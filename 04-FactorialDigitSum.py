# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

import math

# create a function to get the factorial of 100 and also calculate the sum of digits in the factorial
def factorial(n):
    
    fact = math.factorial(n) # importing a function that calculates the factorial of n
    print("Factorial of ", n, "is: ", fact)

    x = str(fact) # changing factorial from int to string
    # Ref: https://stackoverflow.com/questions/6429638/how-to-split-a-string-into-integers-in-python
    s = [int(i) for i in str(x)] # taking the string and putting it into an array while splitting it into integers using loop
    print("Sum of digits in the number 100! is: ", sum(s)) # print out the sum of integers in array


    

factorial(100) # call the function