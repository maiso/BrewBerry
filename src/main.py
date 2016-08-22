'''
Created on Aug 17, 2016

@author: maiso
'''
import pidGUI
import wx
import OneWireInterface
#import Servo


import time, threading
import datetime
UpdateGraph = None

def StartTemperatureLoop():
    global UpdateGraph
    print datetime.datetime.now()
    print 'AAAAA' 
    temperature = StartTemperatureLoop.temp.read_temp()
    if(temperature != None):
        UpdateGraph(temperature)
    threading.Timer(1, StartTemperatureLoop).start()

app = wx.App()
#serv = Servo.Servo()
wxApp = pidGUI.MyFrameSub(None)
#wxApp.CreatePlot()
tempSnor = OneWireInterface.OneWireSensor()
StartTemperatureLoop.temp = tempSnor
UpdateGraph = wxApp.UpdateGraph
StartTemperatureLoop()
wxApp.Show()
app.MainLoop()
   

