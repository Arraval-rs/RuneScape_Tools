#####################################################
# RsArch_toBuild.py                             	#
# Code for the implementation of the to build tab  	#
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Creating layouts for each faction's artefacts
armadyl_frame = RsA_f.create_item_frame("Armadylean", "To Build", "Artefacts")
bandos_frame = RsA_f.create_item_frame("Bandosian", "To Build", "Artefacts")
dragonkin_frame = RsA_f.create_item_frame("Dragonkin", "To Build", "Artefacts")
saradomin_frame = RsA_f.create_item_frame("Saradominist", "To Build", "Artefacts")
zamorak_frame = RsA_f.create_item_frame("Zamorakian", "To Build", "Artefacts")
zaros_frame = RsA_f.create_item_frame("Zarosian", "To Build", "Artefacts")

toBuild_tab = [[
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