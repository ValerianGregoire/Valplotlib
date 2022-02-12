# This is an example program
# We'll display the cos and sin functions from -5 to 30

# We start by importing the libraries we need
import valplotlib as val
import numpy as np

# We start by creating our graph
graph1 = val.graph()

# Let's define the title of the graph and color it to purple for example
graph1.title.name = 'Tan(x) on [-5;30]'
graph1.title.size = 20
graph1.title.color = 'magenta'

# Let's define the x axis now
graph1.xaxis.min = -5
graph1.xaxis.max = 30
graph1.xaxis.name = 'The X axis'
graph1.xaxis.size = 12
graph1.xaxis.step = 7

# Let's do the same for the y axis
graph1.yaxis.min = -2
graph1.yaxis.max = 2
graph1.yaxis.name = 'The Y axis'
graph1.yaxis.size = 10
graph1.yaxis.step = 0.3

# Let's add a legend to the graph and remove its frame
graph1.legend.state = True
graph1.legend.frame = False
graph1.legend.position = 'upper left'

# Let's add a grid to the graph
graph1.grid = True

# Let's display the graph without any content now
# The first graph displayed has the right shape but is empty
graph1.display()
# The console prints "No handles with labels found to put in legend."
# It's because there is no figure to add to the legend yet


# Let's create two figures to display in the graph 

# We start by creating values for x and y with numpy library
x_values = np.arange(-5,30,0.1)
y1_values = np.cos(x_values)
y2_values = np.sin(x_values)

# We then create and customize a line object
curve1 = val.line()
curve1.x = x_values
curve1.y = y1_values
curve1.color = 'cyan'
curve1.width = 2
curve1.style = '--'
curve1.name = 'Line object'


# Create the second figure to display. This one will be a scatter
curve2 = val.scatter()
curve2.x = x_values
curve2.y = y2_values
curve2.color = 'red'
curve2.size = 8
curve2.style = 'o'
curve2.name = 'Scatter object'

# We create a list of the lines to display.
# Note that in real conditions, a large amount of curves could
figureslist = [curve1, curve2]

# We add the list of figures to the graph
graph1.bulkfigureinsert(figureslist)

# The last step is to display the graph we created
graph1.display()

# Now let's say we want to remove the first figure of the plots
graph1.figureremove(curve1)

# Let's display the plot we get one last time
graph1.display()



print("")
print("----- Example program -----")
print("Make sure to check out the three graphs created")