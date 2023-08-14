#####################################################
# RsArch_artefacts.py                             	#
# Code for the implementation of the artefacts tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f
import generalFunctions as func

class ArtefactTab:
	def __init__(self):
		# Creating layouts for each faction's artefacts
		armadyl_frame = self.create_artefact_frame("Armadylean")
		bandos_frame = self.create_artefact_frame("Bandosian")
		dragonkin_frame = self.create_artefact_frame("Dragonkin")
		saradomin_frame = self.create_artefact_frame("Saradominist")
		zamorak_frame = self.create_artefact_frame("Zamorakian")
		zaros_frame = self.create_artefact_frame("Zarosian")

		self.layout = [[
							sg.Column(
								[
									[sg.Frame("Armadylean", armadyl_frame)],
									[sg.Frame("Bandosian", bandos_frame)],
									[sg.Frame("Dragonkin", dragonkin_frame)],
									[sg.Frame("Saradominist", saradomin_frame)],
									[sg.Frame("Zamorakian", zamorak_frame)],
									[sg.Frame("Zarosian", zaros_frame)]
								], element_justification = "center", size = (300,300), scrollable = True, vertical_scroll_only = True)
						]]

	def create_artefact_frame(self, faction):
		frame = [[]]
		for i in range(0, 5):
			column = []
			for j in range(0, int(len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts", faction]))/5+0.5)):
				if i+5*j < len(RsA_f.read_value(RsA_f.arch_dict,["Artefacts", faction])):
					artefact_name = RsA_f.read_value(RsA_f.arch_dict,['Artefacts',faction,i+5*j,'Name'])
					column.append([sg.Image(data = func.generate_image(f"images/artefacts/{artefact_name} (damaged).png", (31, 31), True), tooltip = artefact_name)])
					column.append([sg.Input(default_text = RsA_f.read_value(RsA_f.arch_dict, ["Artefacts", faction, i+5*j, "Stored"]), enable_events = True, justification = "right", size = (3, 1), key = f"{faction}Artefacts_{i+5*j}")])
				else:
					column.append([sg.Sizer(31, 66)])
			frame[0].append(sg.Column(column, element_justification = 'center'))
		return frame

	# function for Artefacts tab events
	def artefact_events(self, window, event):
		return	