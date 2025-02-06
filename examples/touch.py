from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks

@inlineCallbacks
def main(session, details):
    
	yield session.call("rom.optional.behavior.play", name="BlocklyStand")
	yield session.call("rie.dialogue.say_animated", text="Hello, I am Alphamini number 4!", lang="en")
		  
	def touched(frame):

		if ("body.head.front" in frame["data"] and frame["data"]["body.head.front"]):
			session.call("rie.dialogue.say", text="UUUU sunny!")
			print("Front sensor")
   
		elif ("body.head.middle" in frame["data"] and frame["data"]["body.head.middle"]):
			session.call("rie.dialogue.say", text="Bleach it's raining!")
			print("Middle sensor")
   
		elif ("body.head.rear" in frame["data"] and frame["data"]["body.head.rear"]):
			session.call("rie.dialogue.say", text="I like the clouds touching my face!")
			print("Rear sensor")

		# yield session.call("rom.optional.behavior.play", name="BlocklyCrouch")
	
	yield session.subscribe(touched, "rom.sensor.touch.stream")
	# yield session.leave()
	yield session.call("rom.sensor.touch.stream")

wamp = Component(
	transports=[{
		"url": "ws://wamp.robotsindeklas.nl",
		"serializers": ["msgpack"],
		"max_retries": 0
	}],
	realm="rie.67a48ccc85ba37f92bb13c92",
)

wamp.on_join(main)

if __name__ == "__main__":
	run([wamp])