# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Michal Sleszynski

Demonstrating Hierarchical Inheritance

When more than one derived class are created from a single base this 
type of inheritance is called hierarchical inheritance

"""

# Base class `Player`
class Player:
    def __init__(self, ingameid, level):
        self.ingameid = ingameid
        self.level = level
 
    def display_details(self):
        return f"GameID: {self.ingameid}, Level: {self.level}"
 
# Two derived classes, `Officer` and `Master`
class Officer(Player):
    # this class includes a `team_size` attribute
    def __init__(self, ingameid, level, team_size):
        super().__init__(ingameid, level)
        self.team_size = team_size
 
# `display_details` methods are invoked to display 
# specific information for the classes
    def display_details(self):
        return f"{super().display_details()}, Party Size: {self.team_size}"
 
class Master(Player):
    # this class has a `team name` attribute
    def __init__(self, ingameid, level, team_name):
        super().__init__(ingameid, level)
        self.team_name = team_name
 
    def display_details(self):
        return f"{super().display_details()}, Team Name: {self.team_name}"
 
# Instances officer and master of both classes are created
officer = Officer("Maxus12", 80, 10)
master = Master("TPandaZz", 100, "PXG")
print(officer.display_details())    
print(master.display_details()) 