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
        # yield self.session.subscribe(self.vision, "rom.sensor.sight.read")
        frames = yield self.session.call("rom.sensor.sight.read", ubi=["body.head.eyes"], time=1000)
       
        for frame in frames:
            emotion = self.vision(frame.get("data").get("body.head.eyes"))
            if emotion == "confused":
                return"confused"
            
        return "not confused"

    def vision(self, frame):
        if frame is None:
            return
        image = Image.open(io.BytesIO(frame))
        predictions = self.pipe(image)
        dominant_emotion = max(predictions, key=lambda x: x["score"])
        if dominant_emotion["label"] == "neutral" or dominant_emotion["label"] == "happy":
            emotion = "not confused"
        else:
            emotion = "confused"
        return emotion
            
                
            
    def get_emotion(self):
        return self.emotion
    
    def reset_emotion(self):
        self.emotion = None     
    
