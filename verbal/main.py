import os

from alpha_mini_rug.speech_to_text import SpeechToText
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks


class GameMaster:
    def __init__(self, session):
        self.session = session
        self.audio_processor = SpeechToText()
        self.audio_processor.silence_time = 0.5  # when to stop recording
        self.audio_processor.silence_threshold2 = (
            100  # any sound recorded below this value is considered silence
        )
        self.audio_processor.logging = (
            False  # set to true if you want to see all the output
        )

    @inlineCallbacks
    def default_state(self):
        yield self.session.call("rom.optional.behavior.play", name="BlocklyStand")
        
    @inlineCallbacks
    def start_game(self):
        yield self.dialogue()

    def end_game(self):
        self.session.leave()

    @inlineCallbacks
    def play_game(self):
        yield self.start_game()
        self.end_game()

    @inlineCallbacks
    def dialogue(self):
        # Define the file path
        output_dir = "output"
        output_file = os.path.join(output_dir, "output.wav")

        # Create the directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Create the file if it doesn't exist
        if not os.path.exists(output_file):
            with open(output_file, "wb") as f:
                f.write(b"")

        # Write an empty byte string to create the file
        yield self.STT_continuous()

    @inlineCallbacks
    def STT_continuous(self):
        info = yield self.session.call("rom.sensor.hearing.info")
        print(info)

        yield self.session.call("rom.sensor.hearing.sensitivity", 1650)
        yield self.session.call("rie.dialogue.config.language", lang="en")
        yield self.session.call("rie.dialogue.say", text="Say something")
        print("listening to audio")

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
                print("I'm processing the words")
                print(word_array)  # print last 3 sentences
                

            self.audio_processor.loop()

@inlineCallbacks
def main(session, details):
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
    realm="rie.67a489ba85ba37f92bb13c72",
)

wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
