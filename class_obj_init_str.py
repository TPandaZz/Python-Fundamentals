# -*- coding: utf-8 -*-
"""
Created on Mar 9

@author: Michal Sleszynski

 __init__() function to assign values to object properties
 
__str__() function controls what should be returned 
when the class object is represented as a string
"""

class Person:
# self parameter is a reference to the current instance of the class
# and is used to access variables that belong to the class.
# it can be named anything 
  def __init__(self, name, age):
    self.name = name
    self.age = age

# string representation of an object
  def __str__(self):
    return f"{self.name}({self.age})"

# method in the Person class
  def myfunc(self):
    print(f"Hello my name is {self.name} and i am {self.age} years old")

p1 = Person("Michal", 27)
p1.myfunc()
# print(p1)

# *********************************************************
class Person2:
  def __init__(someobject, name, age):
    someobject.name = name
    someobject.age = age

  def myfunc2(abc):
    print(f"Hello my name is {abc.name} and i am {abc.age} years old")

p2 = Person2("Michal", 27)
p2.myfunc2()