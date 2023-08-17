#####################################################
# RsArch_toBuild.py                             	#
# Code for the implementation of the to build tab  	#
#####################################################

import os, io, json, math
import PySimpleGUI as sg
import RsArch_functions as RsA_f
import generalFunctions as func

class ToBuildTab:
	def __init__(self):
		# Creating layouts for each faction's artefacts
		armadyl_frame = self.create_build_frame("Armadylean")
		bandos_frame = self.create_build_frame("Bandosian")
		dragonkin_frame = self.create_build_frame("Dragonkin")
		saradomin_frame = self.create_build_frame("Saradominist")
		zamorak_frame = self.create_build_frame("Zamorakian")
		zaros_frame = self.create_build_frame("Zarosian")

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

	def create_build_frame(self, faction):
		frame = [[]]
		for i in range(0, 5):
			column = []
			for j in range(0, math.ceil(len(RsA_f.artefacts)/5)):
				if i+5*j < len(RsA_f.artefacts[faction]):
					artefact_name = list(RsA_f.artefacts[faction])[i+5*j].name
					column.append([sg.Image(data = func.generate_image(f"images/artefacts/{artefact_name} (damaged).png", (31, 31), True), tooltip = artefact_name)])
					column.append([sg.Input(default_text = "0", justification = "right", size = (3, 1), readonly = True, key = f"{faction}ToBuild_{i+5*j}")])
				else:
					column.append([sg.Sizer(31, 66)])
			frame[0].append(sg.Column(column, element_justification = 'center'))
		return frame