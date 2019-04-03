#MenuTitle: Select all Anchors and Paths
# -*- coding: utf-8 -*-
__doc__="""
Select all Anchors and Paths 90 left in the current glyph.
"""



thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs
thisDoc = Glyphs.currentDocument # the frontmost document

def process( thisLayer ):
	thisLayer.clearSelection()

	for thisAnchor in thisLayer.anchors:
		thisAnchor
		thisLayer.addSelection_(thisAnchor)
	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:
			thisLayer.addSelection_(thisNode)



thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	print "Selecting all anchors and paths in: %s." % thisGlyph.name
	thisGlyph.beginUndo() # begin undo grouping
	process( thisLayer )
	thisGlyph.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View