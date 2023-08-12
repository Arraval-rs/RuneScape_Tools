#####################################################
# RsArch_mats.py                                    #
# Code for the implementation of the materials tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Creating layouts for each faction's materials
agnostic_frame = RsA_f.create_item_frame("Agnostic", "Materials", "Materials")
armadyl_frame = RsA_f.create_item_frame("Armadylean", "Materials", "Materials")
bandos_frame = RsA_f.create_item_frame("Bandosian", "Materials", "Materials")
dragonkin_frame = RsA_f.create_item_frame("Dragonkin", "Materials", "Materials")
saradomin_frame = RsA_f.create_item_frame("Saradominist", "Materials", "Materials")
zamorak_frame = RsA_f.create_item_frame("Zamorakian", "Materials", "Materials")
zaros_frame = RsA_f.create_item_frame("Zarosian", "Materials", "Materials")

materials_tab = [[
					sg.Column(
						[
							[sg.Frame("Agnostic", agnostic_frame)],
							[sg.Frame("Armadylean", armadyl_frame)],
							[sg.Frame("Bandosian", bandos_frame)],
							[sg.Frame("Dragonkin", dragonkin_frame)],
							[sg.Frame("Saradominist", saradomin_frame)],
							[sg.Frame("Zamorakian", zamorak_frame)],
							[sg.Frame("Zarosian", zaros_frame)]
						], element_justification = "center", size = (300,300), scrollable = True, vertical_scroll_only = True)
				]]

# function for Materials tab events
def material_events(window, event):
	return	