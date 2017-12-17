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

####

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    
    agents.append(agentframework.Agent(environment,agents,x,y))
   
carry_on = True	 

####

def update(frame_number):
    
    fig.clear()   
    global carry_on    
   
    #Move each agent
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents) #move agents in a different order each time
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
####
     if agents[i].store > total_fill:
        carry_on = False #changes whether or not to carry on
        print("stopping condition. Final coordinates =")

        #write data_eaten.csv file with amount stored by agents
        s = 0
        for agent in agents:
            s += agent.store #sum agent store
        f3 = open('data_eaten.csv', 'a', newline = '')
        writer = csv.writer(f3, delimiter = ',')
        f3.write(str(s) + "\n") #write new entries to a new line
        f3.close() #realease file after use  
    
####

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    if random.random() < 0.001:
        carry_on = False
        print("stopping condition")
               
#plotting scatter
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        print (agents [i].x, agents [i].y)
        
####

def gen_function(b = [0]):
    
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
####

# animation function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)
    canvas.show()


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
