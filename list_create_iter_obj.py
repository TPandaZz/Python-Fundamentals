# -*- coding: utf-8 -*-
"""
 Created on Feb 29

 @author: Michal Sleszynski

 Create a list to show 10 powers of 2 from an iterator object
 
 To create an object/class as an iterator you have to implement the 
 methods __iter__() and __next__() to the object
"""

# An iterable user defined type
class PowTwo:
    # Constructor
    def __init__(self, max):
        self.max = max
    
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.num = 0
        return self
    
    # To move to next element use __next_
    def __next__(self):
        # To prevent the iteration from going on forever use the StopIteration
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        
        # Else increment and return old value
        self.num += 1
        return result

pow_two = PowTwo(10)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))