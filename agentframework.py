# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:05:34 2017

@author: gy17gjm
"""
#importing
import random


#creating agent class
class Agent() :   
#creating random x and y figures for a graph
   # def __init__(self, environment, agents):
       #self.agents = agents
       #self.environment = environment
       #self.w = len(environment[0])
       #self.h = len(environment)
       #self.x = random.randint(0,self.w - 1) 
      # self.y = random.randint(0,self.h - 1) 
      
    def __init__(self,environment,agents,x=None,y=None):
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y

        self.environment = environment 
        self.agents = agents
        self.w = len(environment[0])
        self.h = len(environment)
        self.x = random.randint(0,self.w - 1) 
        self.y = random.randint(0,self.h - 1)         
        self.store = 0  

            
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x +1) % self.w
        else:
           self.x = (self.x -1) % self.w
           

        if random.random() <0.5:
            self.y = (self.y +1) % self.h
        else: 
            self.y = (self.y -1) % self.h
            

     
    def talk(self) :
        self.agents[0].whatever()
    
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 


 #loop the neighbourhood through self.agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
 #calculate the distance between self and other agents           
            dist = self.distance_between(agent) 
        if dist <= neighbourhood:
#sum self.store & agent.store            
            sum = self.store + agent.store
#divide sum by 2 to for average
            ave = sum /2
            self.store = ave
            agent.store = ave
            print("sharing " + str(dist) + " " + str(ave))
            
            
            
#pythagoras theory
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5