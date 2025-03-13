import io

from autobahn.twisted.component import Component, run
from deepface import DeepFace
from dotenv import load_dotenv
from tqdm import tqdm
from PIL import Image
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = "rie.67d2b12999b259cf43b05316"


class EmotionHandler:
    def __init__(self, session):
        self.emotion = None
        self.frame_count = 0
        self.session = session

    @inlineCallbacks
    def you_shall_see(self):
        yield self.session.subscribe(self.vision, "rom.sensor.sight.stream")
        yield self.session.call("rom.sensor.sight.stream")

    def vision(self, frame):
        self.frame_count += 1
        if self.frame_count % 10 == 0:
            image = Image.open(io.BytesIO(frame["data"]["body.head.eyes"]))
            image.save("image.jpg")
            face_analysis = DeepFace.analyze(
                img_path="image.jpg",
                actions=["emotion"],
                detector_backend="opencv",
            )
            self.emotion = face_analysis["dominant_emotion"]
            print(self.emotion)


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
