# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

import random # import random package to use random function

# random function generates a random number between 1 and 100 and store in num.
num = random.randint(0, 101)

print ("Guess a number between 1 and 100")

guessCount = 0 # counter to count the number of guesses 

# create a while loop for user to guess multiple times
while True:
    guess = input() # user's guess is stored as int in guess
    guess = int(guess)
    guessCount += 1 # increment count by + 1 for every guess

    if guess < num: #if user's guess is less than random num then..
        print("Too low")

    elif guess > num: #if guess is bigger than number then..
        print("Too high")

    elif guess == num: #user guess equals number then..
        print("Winner winner chicken dinner!")
        print("Guesses taken: " , guessCount)
        break # end the while loop 



