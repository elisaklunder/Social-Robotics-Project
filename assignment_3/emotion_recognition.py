import io
import os

from autobahn.twisted.component import Component, run
from dotenv import load_dotenv
from PIL import Image
os.environ["TQDM_DISABLE"] = "1"
from transformers import pipeline
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = os.getenv("REALM")


class EmotionRecognition:
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
        yield self.session.call("rom.sensor.sight.read")

    def vision(self, frame):
        self.frame_count += 1
        if self.frame_count % 10 == 0:
            image = Image.open(io.BytesIO(frame["data"]["body.head.eyes"]))
            
            predictions = self.pipe(image)
            dominant_emotion = max(predictions, key=lambda x: x["score"])
            if dominant_emotion["label"] == "neutral" or dominant_emotion["label"] == "happy":
                self.emotion = "not confused"
            else:
                self.emotion = "confused"
                
                
            
    def get_emotion(self):
        return self.emotion
    
    def reset_emotion(self):
        self.emotion = None     
    
