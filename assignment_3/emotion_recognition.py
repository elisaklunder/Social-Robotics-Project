import io
import os

from autobahn.twisted.component import Component, run
from dotenv import load_dotenv
from PIL import Image
os.environ["TQDM_DISABLE"] = "1"
from transformers import pipeline
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = "rie.67d2b12999b259cf43b05316"


class EmotionHandler:
    def __init__(self, session):
        self.emotion = None
        self.frame_count = 0
        self.session = session
        self.pipe = pipeline(
            "image-classification",
            model="dima806/facial_emotions_image_detection",
            use_fast=True,
        )

    @inlineCallbacks
    def you_shall_see(self):
        yield self.session.subscribe(self.vision, "rom.sensor.sight.stream")
        yield self.session.call("rom.sensor.sight.stream")

    def vision(self, frame):
        self.frame_count += 1
        if self.frame_count % 10 == 0:
            image = Image.open(io.BytesIO(frame["data"]["body.head.eyes"]))
            predictions = self.pipe(image)
            domnant_emotion = max(predictions, key=lambda x: x["score"])
            print(domnant_emotion["label"])


@inlineCallbacks
def main(session: Component, details):
    game_master = EmotionHandler(session)
    yield game_master.you_shall_see()


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
