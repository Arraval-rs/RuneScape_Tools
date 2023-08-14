#####################################################
# RsArch_toBuy.py                             		#
# Code for the implementation of the to buy tab  	#
#####################################################

import os
import io
import json
import PySimpleGUI as sg
import RsArch_functions as RsA_f

# Creating layouts for each faction's materials
agnostic_frame = RsA_f.create_item_frame("Agnostic", "To Buy", "Materials")
armadyl_frame = RsA_f.create_item_frame("Armadylean", "To Buy", "Materials")
bandos_frame = RsA_f.create_item_frame("Bandosian", "To Buy", "Materials")
dragonkin_frame = RsA_f.create_item_frame("Dragonkin", "To Buy", "Materials")
saradomin_frame = RsA_f.create_item_frame("Saradominist", "To Buy", "Materials")
zamorak_frame = RsA_f.create_item_frame("Zamorakian", "To Buy", "Materials")
zaros_frame = RsA_f.create_item_frame("Zarosian", "To Buy", "Materials")

toBuy_tab = [[
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