import matplotlib.pyplot as plt
import numpy as np

class graph:
    
    def __init__(self, fs = None, tn = "", tc = (0,0,0), ts = 20, xan = "", xami = 0,
                xamx = 10, xast = 1, xac = (0,0,0), xasi = None, yan = "", yami = 0, yamx = 10, 
                 yast = 1, yac = (0,0,0), yasi = None, g = False, l = False, lp = "best", lf = True,
                 lc = 1, ):
        
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
        self.xaxis.step = xast
        self.xaxis.color = xac
        self.xaxis.size = xasi
        
        # y axis of the plot
        self.yaxis = Yaxis()
        self.yaxis.name = yan
        self.yaxis.min = yami
        self.yaxis.max = yamx
        self.yaxis.step = yast
        self.yaxis.color = yac
        self.yaxis.size = yasi
        
        # legend of the plot
        self.legend = legend()
        self.legend.state = l
        self.legend.position = lp
        self.legend.columns = lc
        self.legend.frame = lf
        
        # Whether the grid is on or not
        self.grid = g
        
        # list of plots
        self.plotlist = list()
    
    def display(self):
        plt.figure(figsize = self.size)
        
        for element in self.plotlist:
            element.update()
            
            
        plt.title(f'{self.title.name}', c=self.title.color, size=self.title.size)
        
        plt.xlabel(f'{self.xaxis.name}', c=self.xaxis.color, size=self.xaxis.size)
        plt.xlim(self.xaxis.min,self.xaxis.max)
        plt.xticks(np.arange(self.xaxis.min,self.xaxis.max+1e-10,self.xaxis.step)),(np.arange(self.xaxis.min,self.xaxis.max,self.xaxis.step))

        
        
        plt.ylabel(f'{self.yaxis.name}')
        plt.ylim(self.yaxis.min,self.yaxis.max)
        plt.yticks(np.arange(self.yaxis.min,self.yaxis.max+1e-10,self.yaxis.step)),(np.arange(self.yaxis.min,self.yaxis.max,self.yaxis.step))

        if self.legend.state == True:
            plt.legend(loc = self.legend.position, frameon = self.legend.frame)


        
        plt.grid(self.grid)
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



class graphname:
    
    def __init__(self):
        self.color = None
        self.size = None
        self.name = None
        
class legend:

    def __init__(self):
        self.position = None
        self.state = None
        self.frame = None
        self.columns = None
        
        
# Definition of the axes of a graph
class Xaxis:
    
    def __init__(self):
        self.name = None
        self.min = None
        self.max = None
        self.step = None
        self.color = None
        self.size = None
        self.scale = None
        

class Yaxis:
    
    def __init__(self):
        self.name = None
        self.min = None
        self.max = None
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
        
        
        
        
