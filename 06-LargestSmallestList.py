# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

# create a function to determine largest & smallest elements in a list
def func():
    list = [] # initialising array list

    print("Enter number of elements")
    listnum = int(input()) # taking in user input as integer

    # loop through the list
    for i in range(listnum):
        print("Enter element to list: ")
        elements = int(input()) # taking in list elements
        list.append(elements) # appending elements to list

    print("Largest element in the list: ", max(list))
    print("Smallest element in the list: ", min(list))

func() # call function to run