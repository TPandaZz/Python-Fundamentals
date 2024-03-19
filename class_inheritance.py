# -*- coding: utf-8 -*-
"""
Created on Mar 17

@author: Michal Sleszynski

Demonstrating single class inheritance 

super() function is a function that returns the objects that
represent the parent class. It allows to access the parent class’s methods 
and attributes in the child class.

Here create the object ‘obj’ of the child class
call the constructor of the child class Player
initialize the data members to the values at object creation 
use the super() function, invoke the constructor of the parent class
"""

# parent class
class Person():
 
    # the __init__() method is called the constructor 
    # it is always called when an object is created
    # parametrized constructor
    def __init__(self, name, ingameid):
        self.name = name
        self.ingameid = ingameid
 
    def display(self):
        print(self.name, self.ingameid)
 
# child class
class Player(Person):
    def __init__(self, name, ingameid, charclass, level):
        self.sname = name
        self.singameid = ingameid
        self.scharclass = charclass 
        self.level = level 
 
        # inheriting the properties of parent class
        super().__init__(name, "Maxus12")
 
    def displayInfo(self):
        print(self.sname, self.singameid, self.scharclass, self.level)
    
# creation of an object variable or an instance
obj = Player('Michal', 'TPandaZz', 'Python Master', 1)
 
# calling a function of the class Person using its instance
print(obj.display())
print(obj.displayInfo())