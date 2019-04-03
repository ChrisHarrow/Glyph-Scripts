#MenuTitle: Select All Anchors
# -*- coding: utf-8 -*-
__doc__="""
Select all anchors in the current glyph.
"""



thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs
thisDoc = Glyphs.currentDocument # the frontmost document

def process( thisLayer ):
	thisLayer.clearSelection()
	for thisAnchor in thisLayer.anchors:
		thisLayer.addSelection_(thisAnchor)

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	print "Selecting all anchors in: %s." % thisGlyph.name
	thisGlyph.beginUndo() # begin undo grouping
	process( thisLayer )
	thisGlyph.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View