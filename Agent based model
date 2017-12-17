# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:46:57 2017

@author: gy17gjm
"""
#import section
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation
import agentframework #import agentframework file
import csv #csv file library
import requests #access data URL
import bs4 #webscraping
import tkinter #GUI

#####

num_of_agents = 10 
#number of agents created
num_of_iterations = 100
#number of movements allowed per agent
neighbourhood = 20
#maximum distance agents can be to interact
total_fill = 1000
#max data store size

#####
"""
The importation of x and y web data provided, these coordinates are used to form the
agent locations. The extraction of this data is accomplished with the use of beautiful soup
which extracts HTML files.
"""
 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text

# beautiful soup extracts data from HTML file, selecting only y and x
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

print(td_ys) 
print(td_xs)

agents = []
environment = []
#creating empty lists from agents and environment

####
'''
Next, opening the .csv reader code from dowloaded file, converting the file format.
This is followed by arranging the csv data into lists of rows to be used in the environment,
accomplished by appending the rows into the row list. Then the figure is created (7 x & diameter),
with four axes added (left, bottom, width, height), which is scaled to the full extent of the data.
Agents are created to host the x and y coordinates (td_xs/ys), which are granted access to the
environment and other agents.
'''

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


for row in reader:				# A list of rows
    #creating lists of rows for environments
    row_list = []
    #appending and joining the rows into the environment
    for value in row:
        row_list.append (value)
    environment.append(row_list)
 f.close() 


#set up the figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1]) 

#ax.set_autoscale_on(False)


# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    #appending access to the agents
    agents.append(agentframework.Agent(environment,agents,x,y))

# code continues when true
carry_on = True	 

####

"""
The def update generates a new frame for each iteration. Within the frame, the agents 
move randomly, but are restricted t oa fixed number of movements, or iterations, within the 
environment where they eat the data over 10, to place within the store and share with neighbours.
"""

def update(frame_number):
    
    #starts animation
    fig.clear()   
    global carry_on    
   
    #Move each agent
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            #move agents in a different order each time
            random.shuffle(agents) 
  
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
####

"""
The section focused on ending the sequence, which occurs when the data storage is full.
These final coordinates are printed, and stored within 'data_eaten.csv'.
"""
     if agents[i].store > total_fill:
        #changes whether or not to carry on
        carry_on = False 
        print("stopping condition. Final coordinates =")

        #write data_eaten.csv file with amount stored by agents
        s = 0
        for agent in agents:
            #sum agent store
            s += agent.store 
        f3 = open('data_eaten.csv', 'a', newline = '')
        writer = csv.writer(f3, delimiter = ',')
        #write new entries to a new line
        f3.write(str(s) + "\n")
        #realease file after use
        f3.close()   
    
####
"""
The plotting of x & y data between 0-99 coordinated into a figure, and as a scatter graph
printing each iteration.
"""

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
   
    for i in range (num_of_agents):       
        #plotting scatter
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        print (agents [i].x, agents [i].y)
        
####

"""
gen_function determins if the programme should continue to run, or to stop it. 
The run function below then projects the composed files as an animated model, showing the agents
moving within the environment, eating and storing the data.
"""

def gen_function(b = [0]):
    
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
        
# animation function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)
    canvas.show()

####

"""
Building a Graphical User Interface (GUI) using the imported Tkinter. We provide a name for
'Model', menu bar, and command button called 'Run model'.
"""

# main window for GUI
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

#### 

#write dataout.csv with new DEM information
f2 = open('dataout.csv', 'w', newline = '')
writer = csv.writer(f2, delimiter = ',') #, separates values to each cell
for row in environment:
    writer.writerow(row)
f2.close()

#### 

# creates a loop for the GUI
tkinter.mainloop()
