# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Michal Sleszynski

Demonstrating multiple class inheritance

When a child class inherits from multiple parent classes  
"""

# parent class
class Player1(object):
    def __init__(self):
        self.ingameid1 = "Maxus12"
        print("Player1")
        
class Player2():
    def __init__(self):
        self.ingameid2 = "TPandaZz"
        print("Player2")   
    
class Derived(Player1, Player2):
    def __init__(self):
 
        # Calling constructors of Player1
        # and Player2 classes
        Player1.__init__(self)
        Player2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.ingameid1, self.ingameid2)
    
obj = Derived()
obj.printStrs()
 
