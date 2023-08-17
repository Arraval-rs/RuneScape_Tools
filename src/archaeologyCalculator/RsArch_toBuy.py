#####################################################
# RsArch_toBuy.py                             		#
# Code for the implementation of the to buy tab  	#
#####################################################

import os, io, json, math
import PySimpleGUI as sg
import RsArch_functions as RsA_f
import generalFunctions as func

class ToBuyTab:
	def __init__(self):
		# Creating layouts for each faction's materials
		agnostic_frame = self.create_buy_frame("Agnostic")
		armadyl_frame = self.create_buy_frame("Armadylean")
		bandos_frame = self.create_buy_frame("Bandosian")
		dragonkin_frame = self.create_buy_frame("Dragonkin")
		saradomin_frame = self.create_buy_frame("Saradominist")
		zamorak_frame = self.create_buy_frame("Zamorakian")
		zaros_frame = self.create_buy_frame("Zarosian")
		misc_frame = self.create_buy_frame("Miscellaneous")

		self.layout = [[
							sg.Column(
								[
									[sg.Frame("Agnostic", agnostic_frame)],
									[sg.Frame("Armadylean", armadyl_frame)],
									[sg.Frame("Bandosian", bandos_frame)],
									[sg.Frame("Dragonkin", dragonkin_frame)],
									[sg.Frame("Saradominist", saradomin_frame)],
									[sg.Frame("Zamorakian", zamorak_frame)],
									[sg.Frame("Zarosian", zaros_frame)],
									[sg.Frame("Miscellaneous", misc_frame)]
								], element_justification = "center", size = (300,300), scrollable = True, vertical_scroll_only = True)
						]]

	def create_buy_frame(self, faction):
		frame = [[]]
		for i in range(0, 5):
			column = []
			for j in range(0, math.ceil(len(RsA_f.read_value(RsA_f.arch_dict,["Materials", faction]))/5)):
				if i+5*j < len(RsA_f.read_value(RsA_f.arch_dict,["Materials", faction])):
					material_name = list(RsA_f.arch_dict["Materials"][faction])[i+5*j] 
					column.append([sg.Image(data = func.generate_image(f"images/materials/{material_name}.png", (31, 31), True), tooltip = material_name)])
					column.append([sg.Input(default_text = f"{0}", justification = "right", size = (3, 1), readonly = True, key = f"{faction}ToBuy_{i+5*j}")])
					column.append([sg.Input(default_text = f"{0}", justification = "right", size = (3, 1), key = "{}MaterialCost_{}".format(faction, i+5*j))])
				else:
					column.append([sg.Sizer(31, 90)])
			frame[0].append(sg.Column(column, element_justification = 'center'))
		return frame