'''
Created on Aug 17, 2016

@author: maiso
'''
import pidGUI
import wx
import Servo

app = wx.App()
serv = Servo.Servo()
top = pidGUI.MyFrame1(None,serv)
top.Show()
app.MainLoop()
   

