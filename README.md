# Valplotlib
Valplotlib is an attempt to convert the matplotlib library to an intuitive and user-friendly form of OOP.
By doing so, Valplotlib enables sequencial creation of graphs and reuse of figures to plot from a graph to another.

## /!\ This is a work-in-progress project. The aim would be to incorporate the entirety of the matplotlib library into Valplotlib.

### How to use Valplotlib:
Valplotlib splits graphs and figures in objects.




#### You have to create a graph and to customize it along with its axes (that are created when the graph object is created).
To create a graph object, type:
import valplotlib as val
[name of your graph] = val.graph()
The shape and size of the graph can be given by entering a tuple (width,height) when creating the graph object :
[name of your graph] = val.graph((10,20))


The graph object has multiple sub-parts which incorporates attributes that can be modified one by one.
###### For the next few lines, self will refer to the graph object you just created.

self.title designates the title of your graph. You can change name,color,size using self.title.{attribute to change}.
  name is the label of the title.
  If the title is given a name, it will be automatically displayed on your graph.
  color can be defined as a tuple for rgb selection (0,1,0) ranging from 0 to 1. It can also be defined as a string color : 'pink'.
  color works the same for every component throughout this library.

#### self.xaxis designates the x axis of your graph. You can change (name,min,max,step,color,size,scale,start).
  
  min is the starting value of the axis.
  max is the ending value of the axis.
  step is the step between two ticks on the axis
  size designates the size of the font used to display the name of the axis.
  scale should allow you to choose to display the axis with different scales (logarithmic, exponential...) but is probably not working at the moment.
  start is the coordinates of the first point of the grid to display. By default, the grid starts at the first position of x, but you may want it to start at an other value. 
 
#### The exact same commands apply for the y axis using self.yaxis.

#### self.legend is the legend of the graph. You can change (state,position,columns,frame,color,opacity).
  state is a boolean to choose to display the legend or not.
  position, which can be a string or a tupple, choses where the legend is displayed on the graph. As a string, it is possible to write : 'upper left' ; 'lower right'...
  columns indicates with how many columns the elements of the legend should be displayed. By default, the elements are displayed in one column.
  frame is a boolean to indicate whether the legend should have a frame or not.
  color indicates the color of the background of the legend
  opacity, ranging from 0 to 1, sets the transparency of the frame of the legend. Setting it to 0 is the same as setting frame to False.
    
self.grid isn't finished yet. Once finished, it will allow you to customize the grid of your graph.
For now, self.grid is a boolean that toggles the grid on the graph. 
  
#### self.image is the background of the graph. You may give it a path to the image to display.
The image is automatically displayed as a background for your graph.


#### In parallel to the creation of the graph, you may create a line or scatter object.
To create a line or scatter object, you may type :
[name of your line] = val.line()


The line/scatter object has multiple sub-parts which incorporates attributes that can be modified one by one.
###### For the next few lines, self will refer to the line/scatter object you just created.

self.x is the list of x values to which a y value will be attached
self.y is the list of y values to attach to x values
  If the number of x and y values isn't equal, valplotlib may be unable to trace the line.
  
self.style is a string to determine the way the line or scatter should be displayed. Using '--' ; '.' ...
self.size is an integer to indicate the thickness of your line or of your points for a scatter.
self.name gives a name to your line. This name will only be displayed if the legend of the graphs on which it is, is displayed.




#### Once the graphs and lines are created, you will need to attach your lines to the graphs using the graph's figureinsert and bulkfigureinsert methods.
###### For the next few lines, self will refer to the graph object to which you're adding figures.

self.figureinsert(the figure to insert) will add one figure to your graph. You can add multiple figures using a loop.
self.bulkfigureinsert(the list of figures to insert) will add each figure that is contained into a list to your graph. This is the quickest way to create a graph with a lot of figures in it.


#### It is also possible to detach the lines from the graph by using:
self.figureremove(the figure to detach)
self.bulkfigureremove(the list of figure to detach)



#### Once that the graph and the figures are done, and that the figures to display are incorporated in the graph, you need to call the graph's display method to diplay it.
type :
[your graph].display()

#### If everything is done correctly, your graph is displayed in your plot console.
