from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks


@inlineCallbacks
def main(session, details):
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")

    yield session.call(
        "rom.actuator.motor.write",
        frames=[
            {"time": 1000, "data": {"body.arms.right.upper.pitch": -2}},
            {"time": 4000, "data": {"body.arms.right.lower.roll": -1.73}},
            {"time": 6000, "data": {"body.arms.right.lower.roll": -0.1}},
            # {"time": 3000, "data": {"body.arms.right.upper.pitch": -0.3}},

            # {"time": 2000, "data": {"body.arms.right.upper.pitch": -2}},
            # {"time": 3000, "data": {"body.arms.right.upper.pitch": -0.3}},
            
            
        ],
        force=True,
    )
    session.leave()  # Close the connection with the robot


wamp = Component(
    transports=[
        {
            "url": "ws://wamp.robotsindeklas.nl",
            "serializers": ["msgpack"],
            "max_retries": 0,
        }
    ],
    realm="rie.67c189a2a06ea6579d1440f0",
)

wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
