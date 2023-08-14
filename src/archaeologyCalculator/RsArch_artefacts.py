#####################################################
# RsArch_artefacts.py                             	#
# Code for the implementation of the artefacts tab  #
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Creating layouts for each faction's artefacts
armadyl_frame = RsA_f.create_item_frame("Armadylean", "Artefacts", "Artefacts")
bandos_frame = RsA_f.create_item_frame("Bandosian", "Artefacts", "Artefacts")
dragonkin_frame = RsA_f.create_item_frame("Dragonkin", "Artefacts", "Artefacts")
saradomin_frame = RsA_f.create_item_frame("Saradominist", "Artefacts", "Artefacts")
zamorak_frame = RsA_f.create_item_frame("Zamorakian", "Artefacts", "Artefacts")
zaros_frame = RsA_f.create_item_frame("Zarosian", "Artefacts", "Artefacts")

artefacts_tab = [[
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

# function for Artefacts tab events
def artefact_events(window, event):
	return	