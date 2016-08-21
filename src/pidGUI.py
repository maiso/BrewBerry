# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import Servo
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent, serv ):
		self.serv = serv
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,480 ), style = wx.MAXIMIZE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self.m_panel1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( 300,-1 ), wx.SL_AUTOTICKS|wx.SL_BOTH|wx.SL_HORIZONTAL|wx.SL_LABELS )
		gSizer1.Add( self.m_slider1, 0, wx.ALL, 5 )
		
		self.m_radioBtn1 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_gauge1 = wx.Gauge( self.m_panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		gSizer1.Add( self.m_gauge1, 0, wx.ALL, 5 )
		
		self.m_slider1.Bind(wx.EVT_SLIDER, self.OnSliderScroll) 
		
		self.m_panel1.SetSizer( gSizer1 )
		self.m_panel1.Layout()
		gSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def OnSliderScroll(self, e): 
		obj = e.GetEventObject() 
		val = obj.GetValue() 
		self.serv.setAngle(val)

