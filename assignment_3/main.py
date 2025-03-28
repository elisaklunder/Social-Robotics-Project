import os

from alpha_mini_rug import movements
from alpha_mini_rug.speech_to_text import SpeechToText
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from dotenv import load_dotenv
from emotion_handler import EmotionHandler
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
    get_tag_time
)
from process_tags import process_tagged_text, calculate_text_syllables
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = os.getenv("REALM")
RUG_FUNCTION = True

class GameMaster:
    """
    A class that manages the interaction game between a robot and a user.

    This class handles the initialization, execution, and termination of a dialogue-based
    interaction between an Alpha Mini robot and a user. It processes speech input and
    generates appropriate responses using speech-to-text and conversation capabilities.
    """

    def __init__(self, session: Component):
        """
        Initialize Speech Assistant with session and configuration.

        Args:
            session: Session object for robot communication that handles WAMP connections
        """
        self.session = session
        self.audio_processor = SpeechToText()
        self.audio_processor.silence_time = 0.2  # when to stop recording
        self.audio_processor.silence_threshold2 = 100  # hearing threshold
        self.audio_processor.logging = False
        self.conversation_engine = Blabber()
        self.emotion_handler = EmotionHandler(session)

    @inlineCallbacks
    def default_state(self):
        """
        Sets the robot to a default standing position.

        Returns:
            inlineCallbacks: Coroutine that executes the BlocklyStand behavior
        """
        # aa = yield self.session.call("rom.sensor.proprio.read")
        # print(aa)
        yield self.session.call("rom.optional.behavior.play", name="BlocklyStand")

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
        if RUG_FUNCTION: 
            yield movements.perform_movement(self.session, frames=frames, force=True)
        else:
            yield self.session.call("rom.actuator.motor.write", frames=frames, force=True)

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
        yield self.session.call("rie.dialogue.config.language", lang="it")

        self.session.call(
            "rie.dialogue.say",
            text="Ciao, Ai am Alphamini! What's your name?",
            lang="it",
        )
        frames = hi()
        if RUG_FUNCTION: 
            yield movements.perform_movement(self.session, frames=frames, force=True)
        else:
            yield self.session.call("rom.actuator.motor.write", frames=frames, force=True)
        yield sleep(4)
        
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
                # getting the user input
                user_input = word_array[-1] # string

                # checking if the confusion is detected
                # needs to check if the robot is word keeper, and if confusion was detected, and if the answer was negative twice in a row OR answer was negative three times in a row
                
                confusion_detected = self.emotion_handler.is_user_confused()
                print("Is user confused??? ", confusion_detected)
                
                llm_input = f"""
                message {{{user_input}}}
                
                confusion {{{'detected' if confusion_detected else 'not detected'}}}
                """.strip()
                
                llm_answer = self.conversation_engine.ask(llm_input)
                print("answer: ", llm_answer)
                
                self.emotion_handler.detect_positive_response(f"{user_input} \n {llm_answer}")

                tag_positions, cleaned_answer = process_tagged_text(llm_answer)
                frames = make_gestures(tag_positions)
                self.session.call("rie.dialogue.say", text=cleaned_answer, lang="it")

                if frames:
                    if RUG_FUNCTION: 
                        yield movements.perform_movement(self.session, frames=frames, force=True)
                    else:
                        yield self.session.call("rom.actuator.motor.write", frames=frames, force=True)
                    text_syllable_num = calculate_text_syllables(cleaned_answer)
                    sleepy_time = get_tag_time(start_position=text_syllable_num + 13)
                    print(f"sleep time: {sleepy_time}")
                    yield sleep(sleepy_time/1000)
                else:
                    # if there are no frames then the robot should sleep for the entire duration
                    text_syllable_num = calculate_text_syllables(cleaned_answer)
                    sleepy_time = get_tag_time(start_position=text_syllable_num + 13)
                    print(f"sleep time: {sleepy_time}")
                    yield sleep(sleepy_time/1000)
                    
                self.emotion_handler.start_emotion_recognition()

                # The loop continues until a 'goodbye' response is triggered
                if "goodbye" in cleaned_answer.lower():
                    break

            self.audio_processor.loop()

        yield self.session.call("rom.optional.behavior.play", name="BlocklyCrouch")


@inlineCallbacks
def main(session: Component, details):
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
