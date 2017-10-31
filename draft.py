import random
import time

answer=["Good evening", "Hi"]
response=["hi", "good evening"]
answer1=["what you doing?"]
response1=["nothing much", "watching tv", "chatting to people"]

#a
print "Start your chat here\n"
a=raw_input("Annie: ")
time.sleep(.5)

#b
for a in answer:
    #return random.choice(response)    
    print "Julie: " + random.choice(response)

b=raw_input("Annie: ")

for b in response:
    #return random.choice(response1)
    print "Julie: " + random.choice(response1)
