import random
 
print ("Welcome to the coin flipper")
guess = input ("do you guess heads or tails?")
 
x = random.randint(1,2)
 
if x == 1:
 print ("heads")
 
if x == 2:
 print ("tails")
