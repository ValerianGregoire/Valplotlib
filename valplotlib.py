import matplotlib.pyplot as plt
import numpy as np

class graph:
    
    def __init__(self, fs = None, tn = "", tc = (0,0,0), ts = 20, xan = "", xami = 0,
                xamx = 10, xastt = False, xast = 1, xac = (0,0,0), xasi = None, yan = "",
                yami = 0, yamx = 10, yastt = False, yast = 1, yac = (0,0,0), yasi = None,
                g = False, l = False, lp = "best", lf = True, lc = 1, lo = 1, ln = '',
                lcol = (1,1,1), i = None ):
        
        self.size = fs
        
        # Title of the plot
        self.title = graphname()
        self.title.name = tn
        self.title.color = tc
        self.title.size = ts
        
        # x axis of the plot
        self.xaxis = Xaxis()
        self.xaxis.name = xan
        self.xaxis.min = xami
        self.xaxis.max = xamx
        self.xaxis.start = xastt
        self.xaxis.step = xast
        self.xaxis.color = xac
        self.xaxis.size = xasi
        
        # y axis of the plot
        self.yaxis = Yaxis()
        self.yaxis.name = yan
        self.yaxis.min = yami
        self.yaxis.max = yamx
        self.yaxis.start = yastt
        self.yaxis.step = yast
        self.yaxis.color = yac
        self.yaxis.size = yasi
        
        # legend of the plot
        self.legend = legend()
        self.legend.state = l
        self.legend.position = lp
        self.legend.columns = lc
        self.legend.frame = lf
        self.legend.opacity = lo
        self.legend.name = ln
        self.legend.color = lcol
        
        # Whether the grid is on or not
        self.grid = g
        
        # Background of the plot
        self.image = i
        
        # list of plots
        self.plotlist = list()
    
    def display(self):
        # Creation of the plot
        plt.figure(figsize = self.size)
        
        # Insertion of the figures
        for element in self.plotlist:
            element.update()
            
        # Display of the title    
        plt.title(f'{self.title.name}', c=self.title.color, size=self.title.size)
        
        # Display of the background
        if self.image != None:
            self.image = plt.imread(self.image)
            plt.imshow(self.image, extent = [self.xaxis.min,self.xaxis.max,self.yaxis.min,self.yaxis.max], aspect='auto')
        
        # Creation of the x axis
        plt.xlabel(f'{self.xaxis.name}', c=self.xaxis.color, size=self.xaxis.size)
        plt.xlim(self.xaxis.min,self.xaxis.max)
        if self.xaxis.start == False:
            self.xaxis.start = self.xaxis.min
        plt.xticks(np.arange(self.xaxis.start,self.xaxis.max,self.xaxis.step))
        
        # Creation of the y axis
        plt.ylabel(f'{self.yaxis.name}')
        plt.ylim(self.yaxis.min,self.yaxis.max)
        if self.yaxis.start == False:
            self.yaxis.start = self.yaxis.min
        plt.yticks(np.arange(self.yaxis.start,self.yaxis.max,self.yaxis.step))
        
        # Display of the legend
        if self.legend.state == True:
            plt.legend(title = self.legend.name, facecolor = self.legend.color, loc = self.legend.position, frameon = self.legend.frame, framealpha = self.legend.opacity)


        # Display of the grid
        plt.grid(self.grid)
        
        # Display of the plot
        plt.show()
        
        
    def figureinsert(self,figure):
        self.plotlist.append(figure)
        
    def figureremove(self,figure):
        self.plotlist.remove(figure)

    def bulkfigureinsert(self,figlist):
        for fig in figlist:
            self.plotlist.append(fig)
    
    def bulkfigureremove(self,figlist):
        for fig in figlist:
            for element in self.plotlist:
                if fig == element:
                    self.plotlist.remove(element)


# Title class
class graphname:
    
    def __init__(self):
        self.color = None
        self.size = None
        self.name = None
# Legend class      
class legend:

    def __init__(self):
        self.position = None
        self.state = None
        self.frame = None
        self.columns = None
        self.name = None
        self.color = None
        
        
# Definition of the axes of a graph
class Xaxis:
    
    def __init__(self):
        self.name = None
        self.min = None
        self.max = None
        self.start = None
        self.step = None
        self.color = None
        self.size = None
        self.scale = None
        

class Yaxis:
    
    def __init__(self):
        self.name = None
        self.min = None
        self.max = None
        self.start= None
        self.step = None
        self.color = None
        self.size = None
        self.scale = None


# Line object
class line:
    
    def __init__ (self, x = None, y = None, style = None, 
                  width = None, color = 'orange', name = ''):
        
        # line
        self.x = x
        self.y = y
        self.style = style
        self.width = width
        self.color = color
        self.name = name


    def update(self):
        
        plt.plot(self.x,self.y, color = self.color, linewidth = self.width, linestyle = self.style, label = self.name)
        

# Scatter object
class scatter:
    
    def __init__ (self, x = None, y = None, style = None, 
                  size = None, color = 'blue', name = None):
        
        # points
        self.x = x
        self.y = y
        self.style = style
        self.size = size
        self.color = color
        self.name = name


    def update(self):
        
        plt.scatter(self.x,self.y, color = self.color, s = self.size, marker = self.style, label = self.name)
        
# 14/02/22 08:55
