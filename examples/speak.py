from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep

@inlineCallbacks
def main(session, details):
	yield session.call("rom.optional.behavior.play", name="BlocklyStand")
 
	yield session.call("rie.dialogue.say_animated", text="Hello, I am Alphamini number 4!", lang="en")
	yield session.call("rie.dialogue.say_animated", text="Ciao, io sono robotino piccolino numero 4!", lang="it")
 
	yield sleep(2)
	yield session.call("rom.optional.behavior.play", name="BlocklyWaveRightArm")
	session.leave() # Close the connection with the robot

wamp = Component(
	transports=[{
		"url": "ws://wamp.robotsindeklas.nl",
		"serializers": ["msgpack"],
		"max_retries": 0
	}],
	realm="rie.67c18b70a06ea6579d14410e",
)

wamp.on_join(main)

if __name__ == "__main__":
	run([wamp])