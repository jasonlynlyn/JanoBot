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
b = random.choice(response)
if a == b:
    time.sleep(.5) 
    print "Julie: " + random.choice(response)

a1=raw_input("Annie: ")

time.sleep(.5)
print "Julie: " + random.choice(response1)
