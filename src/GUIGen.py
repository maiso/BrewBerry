# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,480 ), style = wx.MAXIMIZE|wx.STAY_ON_TOP|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel_buttons = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,480 ), wx.TAB_TRAVERSAL )
		self.m_panel_buttons.SetMaxSize( wx.Size( 200,480 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( self.m_panel_buttons, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,120 ), 0 )
		self.m_button3.SetMinSize( wx.Size( -1,120 ) )
		self.m_button3.SetMaxSize( wx.Size( 200,120 ) )
		
		bSizer2.Add( self.m_button3, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_button4 = wx.Button( self.m_panel_buttons, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,120 ), 0 )
		self.m_button4.SetMinSize( wx.Size( -1,120 ) )
		self.m_button4.SetMaxSize( wx.Size( 200,120 ) )
		
		bSizer2.Add( self.m_button4, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_button5 = wx.Button( self.m_panel_buttons, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,120 ), 0 )
		self.m_button5.SetMaxSize( wx.Size( 200,-1 ) )
		
		bSizer2.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_button6 = wx.Button( self.m_panel_buttons, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,120 ), 0 )
		self.m_button6.SetMinSize( wx.Size( -1,120 ) )
		self.m_button6.SetMaxSize( wx.Size( 200,120 ) )
		
		bSizer2.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panel_buttons.SetSizer( bSizer2 )
		self.m_panel_buttons.Layout()
		bSizer1.Add( self.m_panel_buttons, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel_mainView = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_mainView.SetMaxSize( wx.Size( 700,480 ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self.m_panel_mainView, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetMaxSize( wx.Size( -1,420 ) )
		
		bSizer9.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.EXPAND, 5 )
		
		self.m_panel8 = wx.Panel( self.m_panel_mainView, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetMinSize( wx.Size( -1,60 ) )
		self.m_panel8.SetMaxSize( wx.Size( -1,60 ) )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Actual Temp" ), wx.VERTICAL )
		
		self.m_ActualTemperature = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ActualTemperature.Wrap( -1 )
		sbSizer1.Add( self.m_ActualTemperature, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer8.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Target Temp" ), wx.VERTICAL )
		
		self.m_TargetTemperature = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_TargetTemperature.Wrap( -1 )
		sbSizer2.Add( self.m_TargetTemperature, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer8.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel8.SetSizer( bSizer8 )
		self.m_panel8.Layout()
		bSizer8.Fit( self.m_panel8 )
		bSizer7.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel_mainView.SetSizer( bSizer7 )
		self.m_panel_mainView.Layout()
		bSizer7.Fit( self.m_panel_mainView )
		bSizer1.Add( self.m_panel_mainView, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

