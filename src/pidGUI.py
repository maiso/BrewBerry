import GUIGen
import wx

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
import matplotlib.animation as manim
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
   
class MyFrameSub(GUIGen.MyFrame1):
    def __init__(self, parent):
        # If we overload __init__ we still need to make sure the parent
        # is initialized.
        GUIGen.MyFrame1.__init__(self, parent)
        self.x =  []
        self.values = []
        #NEW!!
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canv = FigCanvas(self.m_panel2, wx.ID_ANY, self.figure)
        self.animator = manim.FuncAnimation(self.figure,self.anim, interval=1000)
        return

    def anim(self,i):
#        if i%10 == 0:
#            self.values = []
#        else:
#            self.values.append(np.random.rand())
        print self.values
        #print np.arange(1,i%10+1)
        print i
        print '-------'
        self.ax.clear()
        #self.ax.set_xlim([0,10])
        #self.ax.set_ylim([0,100])        
        return self.ax.plot(np.arange(0,len(self.values)),self.values,'r-')
    
    def UpdateGraph(self, new_data):
        self.values.append(new_data)
        #self.x.append(new_data)
        #print self.x
        #y = range(0,len(self.x))
        #print y
        #self.axes.clear()
        #self.axes.plot(self.x, y)
        ##self.line1.set_xdata(self.x)
        ##self.line1.set_ydata(y)
        #self.canvas.draw()
        #self.canvas.Refresh()
        return
       
    def CreatePlot(self):
        self.figure = Figure()#figsize=(6, 4), dpi=100)
        self.axes = self.figure.add_subplot(111)
        #self.line1, = self.axes.plot(x, y, 'r-')
        self.canvas = FigCanvas(self.m_panel2, wx.ID_ANY, self.figure)         
        return
