# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

# create a function for palindrome test
def palindrome():
    word = input("Enter a word: ") # user enters a word and store it in word
    # Reference: https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic
    if str(word) == str(word)[::-1]: # reverses word and checks the location of the string is at 0. if -1 then its not a palindrome.
        print(word, " is a palindrome")
    else:
        print(word, " is NOT a palindrome")

palindrome() # call function to run