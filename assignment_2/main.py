import os

from alpha_mini_rug import movements
from alpha_mini_rug.speech_to_text import SpeechToText
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from dotenv import load_dotenv
from gemini import Blabber
from gestures import (
    arms_lower_default,
    arms_upper_default,
    body_torso_yaw_default,
    head_pitch_default,
    head_roll_default,
    head_yaw_default,
    hi,
    make_gestures,
)
from tagger import process_tagged_text
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = "rie.67c189a2a06ea6579d1440f0"


class GameMaster:
    """
    A class that manages the interaction game between a robot and a user.

    This class handles the initialization, execution, and termination of a dialogue-based
    interaction between an Alpha Mini robot and a user. It processes speech input and
    generates appropriate responses using speech-to-text and conversation capabilities.
    """

    def __init__(self, session):
        """
        Initialize Speech Assistant with session and configuration.

        Args:
            session: Session object for robot communication that handles WAMP connections
        """
        self.session = session
        self.audio_processor = SpeechToText()
        self.audio_processor.silence_time = 0.2  # when to stop recording
        self.audio_processor.silence_threshold2 = 400  # hearing threshold
        self.audio_processor.logging = False
        self.conversation_engine = Blabber()

    @inlineCallbacks
    def default_state(self):
        """
        Sets the robot to a default standing position.

        Returns:
            inlineCallbacks: Coroutine that executes the BlocklyStand behavior
        """
        # yield self.session.call("rom.optional.behavior.play", name="BlocklyStand")
        aa = yield self.session.call("rom.sensor.proprio.read")
        print(aa)

        frames = [
            {
                "time": 0,
                "data": {
                    "body.head.pitch": head_pitch_default,
                    "body.head.yaw": head_yaw_default,
                    "body.head.roll": head_roll_default,
                    "body.arms.right.upper.pitch": arms_upper_default,
                    "body.arms.right.lower.roll": arms_lower_default,
                    "body.arms.left.upper.pitch": arms_upper_default,
                    "body.arms.left.lower.roll": arms_lower_default,
                    "body.torso.yaw": body_torso_yaw_default,
                },
            }
        ]
        yield movements.perform_movement(self.session, frames=frames, force=True)
        # yield self.session.call("rom.actuator.motor.write", frames=frames, force=True)

    @inlineCallbacks
    def start_game(self):
        """
        Initiates the game interaction by starting the dialogue.

        Returns:
            inlineCallbacks: Coroutine that manages the dialogue sequence
        """
        yield self.dialogue()

    def end_game(self):
        """
        Terminates the game by closing the session.
        """
        self.session.leave()

    @inlineCallbacks
    def play_game(self):
        """
        Executes the complete game sequence from start to finish.

        Returns:
            inlineCallbacks: Coroutine that handles the complete game execution
        """
        yield self.start_game()
        self.end_game()

    @inlineCallbacks
    def dialogue(self):
        """
        Sets up and manages the dialogue recording system.

        Returns:
            inlineCallbacks: Coroutine that manages the dialogue recording process
        """
        # Store recording
        output_dir = "output"
        output_file = os.path.join(output_dir, "output.wav")
        os.makedirs(output_dir, exist_ok=True)
        if not os.path.exists(output_file):
            with open(output_file, "wb") as f:
                f.write(b"")

        # Actually record
        yield self.STT_continuous()

    @inlineCallbacks
    def STT_continuous(self):
        """
        Handles continuous speech-to-text processing and robot responses.

        Returns:
            inlineCallbacks: Coroutine that manages the continuous STT process
        """
        info = yield self.session.call("rom.sensor.hearing.info")
        print(info)
        yield self.session.call("rom.sensor.hearing.sensitivity", 1650)
        yield self.session.call("rie.dialogue.config.language", lang="en")

        self.session.call(
            "rie.dialogue.say",
            text="Nice to meet you, I am Alphamini! What's your name?",
        )
        frames = hi()
        yield movements.perform_movement(self.session, frames=frames, force=True)
        # yield self.session.call("rom.actuator.motor.write", frames=hi(), force=True)

        yield self.session.subscribe(
            self.audio_processor.listen_continues, "rom.sensor.hearing.stream"
        )
        yield self.session.call("rom.sensor.hearing.stream")

        while True:
            if not self.audio_processor.new_words:
                yield sleep(0.5)  # VERY IMPORTANT
                print("I am recording")
            else:
                word_array = self.audio_processor.give_me_words()
                print("heard: ", word_array[-1])
                user_input = word_array[-1]
                answer = self.conversation_engine.ask(user_input)
                print("answer: ", answer)

                tag_positions, cleaned_answer = process_tagged_text(answer)
                frames = make_gestures(tag_positions)
                self.session.call("rie.dialogue.say", text=cleaned_answer, lang="en")

                if frames:
                    yield movements.perform_movement(
                        self.session, frames=frames, force=True
                    )
                    # yield self.session.call(
                    #     "rom.actuator.motor.write", frames=frames, force=True
                    # )

                # The loop continues until a 'goodbye' response is triggered
                if "goodbye" in cleaned_answer.lower():
                    break

            self.audio_processor.loop()

        yield self.session.call("rom.optional.behavior.play", name="BlocklyCrouch")


@inlineCallbacks
def main(session, details):
    """
    Main entry point for the robot interaction program.
    Creates a GameMaster instance and executes the game sequence.

    Args:
        session: WAMP session object for robot communication
        details: Additional session details

    Returns:
        inlineCallbacks: Coroutine that manages the main program execution
    """
    game_master = GameMaster(session)
    yield game_master.default_state()
    yield game_master.play_game()


wamp = Component(
    transports=[
        {
            "url": "ws://wamp.robotsindeklas.nl",
            "serializers": ["msgpack"],
            "max_retries": 0,
        }
    ],
    realm=REALM,
)

wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
