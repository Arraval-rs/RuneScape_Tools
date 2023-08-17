#####################################################
# RsArch_collections.py                             #
# Code for the implementation of the collections tab#
#####################################################

import os, io, json, math
import PySimpleGUI as sg
import RsArch_functions as RsA_f
import generalFunctions as func

class CollectionTab:
	def __init__(self):
		# Creating layouts for each faction's artefacts
		armadyl_frame = self.create_collection_frame("Armadylean")
		bandos_frame = self.create_collection_frame("Bandosian")
		dragonkin_frame = self.create_collection_frame("Dragonkin")
		saradomin_frame = self.create_collection_frame("Saradominist")
		zamorak_frame = self.create_collection_frame("Zamorakian")
		zaros_frame = self.create_collection_frame("Zarosian")

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
		return

	def create_collection_frame(self, faction):
		frame = [[]]
		for collection in RsA_f.collections[faction]:
			layout = [[sg.Text(f"Total Cost: {0}"), sg.Checkbox("Enabled", default = collection.enabled)], [sg.Frame("Artefacts", self.format_artefacts(collection.artefacts))], [sg.Frame("Materials", self.format_materials(collection.materials))]]
			frame.append([sg.Frame(f"{collection.name} (Level {collection.level})", layout)])
		return frame

	def format_artefacts(self, data):
		layout = [[]]
		for i in range(0, 5):
			column = []
			for j in range(0, math.ceil(len(data)/5)):
				if(i+5*j < len(data)):
					artefact_name = list(data)[i+5*j]
					column.append([sg.Image(data = func.generate_image(f"images/artefacts/{artefact_name} (damaged).png", (31, 31), True), tooltip = artefact_name)])
				else:
					column.append([sg.Sizer(31, 40)])
			layout[0].append(sg.Column(column, element_justification = 'center'))
		return layout

	def format_materials(self, data):
		layout = [[]]
		for i in range(0, 5):
			column = []
			for j in range(0, math.ceil(len(data)/5)):
				if(i+5*j < len(data)):
					material_name = list(data)[i+5*j]
					column.append([sg.Image(data = func.generate_image(f"images/materials/{material_name}.png", (31, 31), True), tooltip = material_name)])
					column.append([sg.Text(data[material_name]["Count"])])
				else:
					column.append([sg.Sizer(31, 66)])
			layout[0].append(sg.Column(column, element_justification = 'center'))
		return layout