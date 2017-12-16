# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 12:05:34 2017

@author: gy17gjm

This formulated code produces the agent based model required to build the agents
and allow them to move within the envrionment.
""" 

import random

class Agent() :   

# __init__ = constructor: forming self.envrionment; self.agent; self.x(0) & self.y(0) 
    def __init__(self,environment,agents,x=None,y=None):

# If x=(0), randomise between 0-99, or use available x 
        if (x == None):
            self.x = random.randint(0,99)
        else:
            self.x = x

# If y=(0), randomise between 0-100, or use available y 
        if (y == None):
            self.y = random.randint(0,99)
        else:
            self.y = y
            
"""
The __init__ function has defined the different aspects of the agent-based model... 
the environment, agents, x & y; setting both X and Y to none.

By setting x & y to none, or no location, it allows the agent to formulate random
coordinates between 0-99, however it also allows any provided coordinate to be used.

Creating:
environment data (.cvs)

y = random y coordinate between 0-99
x = random x coordinate between 0-99
else
y = set y coordinate
x = set x coordinate
""" 


        self.environment = environment 
        self.agents = agents        
        self.store = 0  

"""
Alters the class name, removing the self. and sets store to zero.
"""


    def move(self):
      
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
           self.x = (self.x - 1) % 100
           

        if random.random() <0.5:
            self.y = (self.y +1) % 100
        else: 
            self.y = (self.y -1) % 100

"""
The move function moves the agent within the formulated environment. The set parameters
makes the randomly positioned coordinates to move randomly + or - 1 space at a time within
the environment.

Creating:
y coordinate moving +/- 1
x coordinate moving +/- 1
"""


   
    def eat(self): 
         
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
"""
This function allows the agents to eat away at the environment DEM. The created function follows:
If the DEM projects a value of > 10, it should remove a value of 10 leaving zero. But adding
10 into the self.store created.
"""


    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
"""
distance_between calculates the distance between agents by using pythagoras theorem 
"""

    def share_with_neighbours(self, neighbourhood):
      
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <=  neighbourhood:
                total = self.store + agent.store
                self.store = total / 2 
                agent.store = total / 2
"""
share_with_neighboroughs allows data to be shared between agents. This is conducted within
the calculcations provided which read...
If agents are within range of the neighbourhood, total the storage from self. and agent., 
and split this equally into two stores.
"""
