# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

# create a function to reverse a string
def reverse():
    word = input("Enter a string: ") #user enters a string and store it in word
    word = word[::-1] # slices and reverses the string
    # Reference: https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    print(word)

reverse() # call function to run
