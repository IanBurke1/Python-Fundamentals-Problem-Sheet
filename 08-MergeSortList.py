# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

# Problem Sheet: https://emerging-technologies.github.io/problems/python-fundamentals.html

# create a function to merge and sort lists
def mergeSort():
    # create two lists
    list1 = [1,4,6]
    list2 = [2,3,5]
    
    list1.extend(list2) # Merge list2 into list1
    list1.sort() # sort the merged lists
    print(list1)

mergeSort() # call function to run



