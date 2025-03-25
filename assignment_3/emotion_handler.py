import io
import os

from autobahn.twisted.component import Component, run
from dotenv import load_dotenv
from PIL import Image

from gemini import Blabber
from emotion_recognition import EmotionRecognition
os.environ["TQDM_DISABLE"] = "1"
from twisted.internet.defer import inlineCallbacks

load_dotenv()
REALM = os.getenv("REALM")


class EmotionHandler:
    def __init__(self, session):
        self.emotion_recognition = EmotionRecognition(session)
        self.llm = Blabber(prompt_file="assignment_3/prompt_detect.txt")
        self.detected_emotion = None
        self.answer_streak = []

    @inlineCallbacks
    def start_emotion_recognition(self):
        self.detected_emotion = yield self.emotion_recognition.you_shall_see()
        print("detected emotion:", self.detected_emotion)   
        
    def detect_positive_response(self, llm_answer):
        detection = self.llm.ask(llm_answer)
        if "true" in detection.lower():
            self.answer_streak.append("True")
        elif "false" in detection.lower(): 
            self.answer_streak.append("False")
        else:
            self.answer_streak.append("None")
        
    def is_user_confused(self):
        confused = False
        
        # if len(self.answer_streak) >= 3:
        #     if self.answer_streak[-3:] == ["False", "False", "False"]:
        #         confused = True
        if len(self.answer_streak) >= 2:
            if self.answer_streak[-2:] == ["False", "False"] and self.detected_emotion == "confused":
                confused = True
                print("CONFUSED")
                
        return confused
        
        

@inlineCallbacks
def main(session: Component, details):
    emotion_handler = EmotionHandler(session)
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


        