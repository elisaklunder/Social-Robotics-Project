import os

from alpha_mini_rug.speech_to_text import SpeechToText
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from dotenv import load_dotenv
from gemini import Blabber
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
        yield self.session.call("rom.optional.behavior.play", name="BlocklyStand")

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

        yield self.session.call(
            "rie.dialogue.say",
            text="Nice to meet you, I am Alphamini! What's your name?",
        )

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
                print(word_array[-1])
                user_input = word_array[-1]
                robot_answer = self.conversation_engine.ask(user_input)

                # The loop continues until a 'goodbye' response is triggered
                if "goodbye" in robot_answer.lower():
                    yield self.session.call(
                        "rie.dialogue.say_animated", text=robot_answer, lang="en"
                    )
                    break

                self.session.call(
                    "rie.dialogue.say_animated", text=robot_answer, lang="en"
                )

            self.audio_processor.loop()

        # When the interaction ends, crouch the robot
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
