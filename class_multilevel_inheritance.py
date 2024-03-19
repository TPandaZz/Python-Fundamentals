# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Michal Sleszynski

Demonstrating multilevel class inheritance

When we have a child and grandchild relationship. 
This means that a child class will inherit from its parent class,
which in turn is inheriting from its parent class.

"""

# Parent class
class Player1(object):
 
    # Constructor
    def __init__(self, ingameid1):
        self.ingameid1 = ingameid1
 
    # To get id
    def getID(self):
        return self.ingameid1
 
# Intermediate class
class Child(Player1):
 
    # Constructor
    def __init__(self, ingameid1, level):
        # invoking constructor of Player class
        Player1.__init__(self, ingameid1)
        self.level = level

    def getLvl(self):
        return self.level
 
# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
  
    def __init__(self, ingameid1, level, character):
        # invoking constructor of Child class
        Child.__init__(self, ingameid1, level)
        self.character = character
 
    # To get address
    def getChar(self):
        return self.character
 
    def print_name(self):
        print('Player ID:', self.ingameid1)
        print("Level:", self.level)
        print("Character:", self.character)
 
# Driver code
g = GrandChild("TPandaZz", 1, "Python-Master")
# print(g.getID(), g.getLvl(), g.getChar())
g.print_name()