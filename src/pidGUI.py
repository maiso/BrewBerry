import GUIGen
import wx

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
import matplotlib.animation as manim
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import numpy as np
   
class MyFrameSub(GUIGen.MyFrame1):
    def __init__(self, parent):
        # If we overload __init__ we still need to make sure the parent
        # is initialized.
        GUIGen.MyFrame1.__init__(self, parent)
        self.x =  []
        self.values = []

        self.figure = Figure(facecolor='w', edgecolor='k')
        self.ax = self.figure.add_subplot(111)
        self.canv = FigureCanvasWxAgg(self.m_panel2, wx.ID_ANY, self.figure)
        self.animator = manim.FuncAnimation(self.figure,self.anim, interval=1000)
        self.figure.set_frameon(False) #Disable background collor, use panel collor
        return

    def anim(self,i):
#        print self.values
#        print i
#        print '-------'
        self.ax.clear()
        #self.ax.set_xlim([0,10])
        self.ax.set_ylim([0,100])        
        if(self.values == None or len(self.values) == 0):
            return
        if(isinstance(self.values[-1], float)):
            self.m_ActualTemperature.SetLabel("{:.2f}".format(self.values[-1]))
        return self.ax.plot(np.arange(0,len(self.values)),self.values,'r-')
    
    def UpdateGraph(self, new_data):
        self.values.append(new_data)
        self.canv.Refresh()
        return