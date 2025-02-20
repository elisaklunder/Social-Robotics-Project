import os

from alpha_mini_rug.speech_to_text import SpeechToText
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from dotenv import load_dotenv
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
from alpha_mini_rug import movements

load_dotenv()
REALM = os.getenv("REALM")

class GestureControl:

    def __init__(self, session):
        self.session = session

    @inlineCallbacks
    def nod(self):
        # Nod yes
        yield movements.perform_movement(self.session,
                     frames=[{"time": 400, "data": {"body.head.pitch": 0.1}},
                             {"time": 1200,"data": {"body.head.pitch": -0.1}},
                               {"time": 2000, "data": {"body.head.pitch": 0.1}},
                                {"time": 2400, "data": {"body.head.pitch": 0.0}}],
                                force=True)

    @inlineCallbacks    
    def shake_head(self):
        # Shake no
        # yaw
        yield movements.perform_movement(self.session,
                     frames=[{"time": 400, "data": {"body.head.yaw": 0.1}},
                             {"time": 1200,"data": {"body.head.yaw": -0.1}},
                               {"time": 2000, "data": {"body.head.yaw": 0.1}},
                                {"time": 2400, "data": {"body.head.yaw": 0.0}}],
                                force=True)
        
    def beat_gesture_1(self):
        pass

    def beat_gesture_2(self):
        pass
    
    def emotional_gesture(self):
        pass


@inlineCallbacks
def main(session, details):
    gestures = GestureControl(session)
    yield gestures.nod()
    session.leave() # Close the connection with the robot


# create wamp connection
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