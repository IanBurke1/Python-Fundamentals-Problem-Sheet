# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

# loop from 1 to 100
for i in range (1, 101):
    
    if i % 3 == 0 and i % 5 ==0: # if the number is evenly divided by 3 with 0 remainder and same with 5 then..
        print("fizzbuzz") #print out fizzbuzz
    elif i % 3 == 0: # if the number is evenly divided by 3 with no remainder "== 0" then..
        print("fizz")
    elif i % 5 == 0: # else if the number is evenly divided by just 5 then
        print("buzz")
    else: # if not above then print the number 
        print(i)