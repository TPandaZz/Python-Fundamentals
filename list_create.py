# -*- coding: utf-8 -*-
"""
 Created on Feb 19

 @author: Michal Sleszynski

_____Practicing Lists_____
- map() - function executes a specified function for each item in an iterable 
    The item is sent to the function as a parameter.
- list() - convert string to list
- set()
- 

- .split() - splits string and stores it in a list
- .strip() - removes spaces and trailing characters
"""

# *** Creating Lists in 3 ways ***

# *********** 1 *************
# Initialize list1 by hand
list1 = [1, 2, 4, 4, 3, 3, 3, 6, 5]

# *********** 2 *************
# Initalize list 2 by storing integers in a list using map, split and strip  
# input the desired size for list2
n = int(input("Enter the size of list :"))
list2 = list2 = list(set(map(int, input("Enter integer elements (use spaces):") \
                     .strip().split())))[:n]
# [:n] slices the list so if too many numbers are typed in
# the list will  only receive the provided n size of elements
# ensure the size of the list = elements of the list
if len(list2) < n:
    print("Number of elements is not equal to the size of list, try again.")
    list2 = list(map(int, input("Enter integer elements:") \
                         .strip().split()))[:n]

# *********** 3 *************
# Initialize list3 by iteration 
list3 = []
for i in range(1,5):
    list3.append(i)

# *********** 4 *************
# Create list by converting string to list
text = "Python"
list_txt = list(text)

# *********** 5 *************
# Create list by converting tuple to list
ltup = (text,)
list_tup = list(ltup)


# *********** 6 *************
# Create list from set
lset = set(ltup)
list_set = list(lset)


# ************************
print(f"List1 elements: {list1}\n")
print(f"List2 elements: {list2}\n")
print(f"List3 elements: {list3}\n")
print(f"List_txt elements: {list_txt}\n")
print(f"List_tup elements: {list_tup}\n")
print(f"List_set elements: {list_set}\n")



