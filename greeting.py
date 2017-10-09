import time, random

first_greeting =("hey","hi", "whats up", "what you doing", "yo")
responses=["nothing much", "im bored", "feeling blue"]

print "Don't be shy. Just say something, anything"
b=raw_input()
time.sleep(1.2)

def greeting(b):
		if b.lower() in first_greeting:
			time.sleep(1.2)
			return random.choice(responses)

greeting(b)
