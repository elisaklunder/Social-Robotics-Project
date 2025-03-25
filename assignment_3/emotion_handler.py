import io
import os

from autobahn.twisted.component import Component, run
from dotenv import load_dotenv
from PIL import Image

from emotion_recognition import EmotionRecognition
os.environ["TQDM_DISABLE"] = "1"
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = os.getenv("REALM")


class EmotionHandler:
    def __init__(self, session):
        self.emotion_recognition = EmotionRecognition(session)

    @inlineCallbacks
    def start_emotion_recognition(self):
        yield self.emotion_recognition.you_shall_see()
        print(self.emotion_recognition.get_emotion())
        

@inlineCallbacks
def main(session: Component, details):
    emotion_handler = EmotionHandler(session)
    for i in range(100):
        yield emotion_handler.start_emotion_recognition()

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


        