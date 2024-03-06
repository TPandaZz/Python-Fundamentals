# -*- coding: utf-8 -*-
"""
 Created on Feb 20

 @author: Michal Sleszynski

Removing multiple items from a List
- enumerate() 
- list slicing 
- for loop 
"""

# ****Removing all odd numbers****
# Initialize list
list1 = [2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
newlist =[]
#print(f"Original list1: {list1}\n")
for i1 in list1:
    if i1 % 2 == 0:
        newlist.append(i1)
print(f"Removing only odd numbers from list1: {newlist}\n")

# ****Removing all even numbers****
# Initialize list
list2 = [2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
# Using list comprehension 
list2 = [i1 for i1 in list2 if i1 % 2 != 0]
print(f"Removing only even numbers from list1: {list2}\n")


# ****Removing all even numbers with enumerate****
# Initialize list
list3 = [2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
# Using enumerate function
list3 = [i1 for i, i1 in enumerate(list3) if i1 % 2 != 0]
print(f"Removing only even numbers from list1 with enumerate(): {list3}\n")


# ****Remove elements by slicing list****
# Initialize list
list4 = [2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
del list4[2:6]
print(f"After removing values from index 2 to 5: {list1}\n")


# ****Remove multiple indexes by slicing list with for loop****
indexes_to_remove = [0, 3, 6]
# Initialize list
list5 = [2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
for i in sorted(indexes_to_remove, reverse = True): 
    del list5[i]
print(f"After removing values at index 0, 3 and 6: {list5}\n")


# ****Remove multiple elements by slicing list with list comprehension****
# Initialize list
list6 = [10, 5, 8, 9, 12, 7, 4, 15] 
#print(f"Original list: {list6}\n")
# Using list comprehension
elements_to_remove = {5, 9, 15}
list6 = [item for item in list6 if item not in elements_to_remove]
print(f"After removing multiple numbers: {list6}\n")

