#MenuTitle: Modify Notes
# -*- coding: utf-8 -*-
__doc__="""
Adds or removes notes from glyphs.
"""

import vanilla

from Foundation import NSPoint


class ModifyNotesWindow( object ):
	def __init__( self ):
		# Window 'self.w':
		windowWidth  = 370
		windowHeight = 60
		windowWidthResize  = 0 # user can resize width by this value
		windowHeightResize = 0   # user can resize height by this value
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Modify Notes", # window title
			minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
			maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
			autosaveName = "com.chrisharrow.ModifyNotesWindow.mainwindow" # stores last window position and size
		)

		# UI elements:
		self.w.text_1 = vanilla.TextBox( (15-1, 12+3, 75, 14), "Note element:", sizeStyle='small' )
		self.w.noteElement = vanilla.EditText( (65, 12, 70, 15+3), "", sizeStyle = 'small')

		# Run Button:
		self.w.addButton = vanilla.Button((65+160, 12+1, 60, 15), "Add", sizeStyle='small', callback=self.AddNote )
		self.w.removeButton = vanilla.Button((65+160+70, 12+1, 60, 15), "Remove", sizeStyle='small', callback=self.RemoveNote )
		self.w.setDefaultButton( self.w.addButton )

		# Open window and focus on it:
		self.w.open()
		self.w.makeKey()

	def AddNote( self, sender ):
		try:
			print "added"
		except:
			return False

		return True

	def RemoveNote( self, sender ):
		try:
			print "removed"
		except:
			return False

ModifyNotesWindow()