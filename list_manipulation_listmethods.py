# -*- coding: utf-8 -*-
"""
 Created on Feb 19

 @author: Michal Sleszynski

_____Practicing Lists_____
.appened() - add element at end of list
.insert() - insert at specific position
.extend() - add multiple elements at end of list
.reverse() - reverse list
.remove() - remove the first occurrence of the searched element
.pop() - removes only the last element of the list or at specified position
sort() - sort list
clear() - remove all elements
"""

# Initialize list1 by hand
list1 = [1, 2, 4, 4, 3, 3, 3, 6, 5]

list2 = []
for i in range(1,5):
    list2.append(i)
    
print(f"List1 elements: {list1}\n")
print(f"List2 elements: {list2}\n")
    
list1.append(7)
print(f"List1 after append: {list1}\n")

list1.insert(3,12)
print(f"List1 after inserting number 12: {list1}\n")

list1.extend(list2)
print(f"List1 after extending list 1 with List2: {list1}\n")

list1.reverse()
print(f"Reversed List1: {list1}\n")

list1.remove(12)
print(f"List1 after removing number 12: {list1}\n")

list1.pop()
print(f"List1 after pop: {list1}\n")

list1.sort()
print(f"Sorted List1: {list1}\n")

list1.clear()
print(f"Cleared List1: {list1}\n")