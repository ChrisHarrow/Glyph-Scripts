#MenuTitle: Anchor based side bearings
# -*- coding: utf-8 -*-
__doc__="""
Set side bearings based on 'LSB root' and 'RSB root' anchors (GUI).
"""

import vanilla

class SetSideBearings(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((275, 40), "Set anchor based side bearings [LSB_root RSB_root]")

		self.w.text_lsb = vanilla.TextBox((15, 12+2, 30, 14), "LSB", sizeStyle='small')
		self.w.lsb_value = vanilla.EditText((45, 12, 50, 19), "0.0", sizeStyle='small')

		self.w.text_rsb = vanilla.TextBox((102, 12+2, 30, 14), "RSB", sizeStyle='small')
		self.w.rsb_value = vanilla.EditText((132, 12, 50, 19), "0.0", sizeStyle='small')

		self.w.setbutton = vanilla.Button((-80, 12+1, -15, 17), "Set", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.setbutton )

		self.w.open()

	def buttonCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		print "Processing %i glyphs..." % len( selectedLayers )


		try:
			lsb_value = float( self.w.lsb_value.get() )
			rsb_value = float( self.w.rsb_value.get() )
		except:
			lsb_value = 0.0
			rsb_value = 0.0

		# print lsb_value, rsb_value #DEBUG

		font = Glyphs.font

		try:
			lsb_root_list = []
			rsb_root_list = []

			for thisLayer in selectedLayers:
			# print "Changing %s in %s..." % (anchor_name, thisLayer.parent.name) #DEBUG

				thisLayer.setDisableUpdates()

				thisLayerID = thisLayer.associatedMasterId

				Components = thisLayer.components

				for thisComponent in Components:

					offsetX = thisComponent.position.x
					offsetY = thisComponent.position.y

					referenceGlyph = font.glyphs[thisComponent.componentName]

					for thisAnchor in referenceGlyph.layers[thisLayerID].anchors:

						if thisAnchor.name == "LSB root":
							if len(thisLayer.paths)>0 or len(thisLayer.components)>0:
								delta = ( thisAnchor.x + offsetX ) - thisLayer.LSB
								lsb_root_list.append( delta )
								#print "Changed LSB in %s to %s." % ( thisLayer.parent.name, lsb_value ) #DEBUG

						if thisAnchor.name == "RSB root":
							if len(thisLayer.paths)>0 or len(thisLayer.components)>0:
								delta = ( thisAnchor.x + offsetX ) - ( thisLayer.width - thisLayer.RSB )
								rsb_root_list.append( delta )
								#print "Changed RSB in %s to %s." % ( thisLayer.parent.name, rsb_value ) #DEBUG

			for thisLayer in selectedLayers:
			# print "Changing %s in %s..." % (anchor_name, thisLayer.parent.name) #DEBUG

				local_lsb = ""
				local_rsb = ""

				if len( thisLayer.anchors ) > 0:
					thisLayer.setDisableUpdates()

					for thisAnchor in thisLayer.anchors:
						if thisAnchor.name == "LSB root":
							if len(thisLayer.paths)>0 or len(thisLayer.components)>0:
								old_LSB = thisLayer.LSB
								delta = thisAnchor.x - old_LSB
								#thisLayer.LSB = lsb_value - delta
								local_lsb = "found"
								local_lsb_value = lsb_value - delta


						if thisAnchor.name == "RSB root":
							if len(thisLayer.paths)>0 or len(thisLayer.components)>0:
								old_RSB = thisLayer.RSB
								delta = thisAnchor.x - ( thisLayer.width - thisLayer.RSB )
								#thisLayer.RSB = delta + rsb_value
								local_rsb = "found"
								local_rsb_value = delta + rsb_value
								# print "Changed RSB in %s to %s." % ( thisLayer.parent.name, rsb_value ) #DEBUG

				if local_lsb == "found":
					thisLayer.LSB = local_lsb_value
					print "Changed LSB in %s to %s." % ( thisLayer.parent.name, local_lsb_value ) #DEBUG
				else:
					thisLayer.LSB = lsb_value - min(lsb_root_list)
					print "Changed LSB in %s to %s." % ( thisLayer.parent.name, lsb_value - min(lsb_root_list) ) #DEBUG

				if local_rsb == "found":
					thisLayer.RSB = local_rsb_value
					print "Changed RSB in %s to %s." % ( thisLayer.parent.name, local_rsb_value ) #DEBUG
				else:
					thisLayer.RSB = max(rsb_root_list) + rsb_value
					print "Changed RSB in %s to %s." % ( thisLayer.parent.name, max(rsb_root_list) + rsb_value ) #DEBUG

		except:
			print "Error: Failed to set side bearings in %s." % ( thisLayer.parent.name )
		finally:
			thisLayer.setEnableUpdates()

		print "Done."

SetSideBearings()