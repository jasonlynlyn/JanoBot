import time, random


opening=("hi","hello","good evening","yo")
reply=["hi","hello","good evening","yo"]
opening2=("whats up", "what you doing?", "what are you working on")
reply2=["nothing much", "playing with my computer", "just composing one of those crazy ideas"]






def greeting(n, relay=10):
	a=raw_input(n)
	time.sleep(.7)
	
	if a in opening:
		time.sleep(.7)
		print random.choice(reply)
	else:
		return "huh?"
	b=raw_input()
	if b in opening2:
		time.sleep(.7)
		print random.choice(reply2)
	c=raw_input()
	if c in reply2:
		time.sleep(.7)
		print "ok"
	else:
		print "why"

greeting("Talk to me:\n")
