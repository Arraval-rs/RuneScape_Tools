#####################################################
# RsArch_main.py                                    #
# Code for the event loop of the application        #
#####################################################
import os
import io
import json
import PySimpleGUI as sg

# RsArch files
import RsArch_functions as RsA_f
from RsArch_collections import collections_tab
from RsArch_materials import materials_tab
from RsArch_artefacts import artefacts_tab
from RsArch_toBuy import toBuy_tab
from RsArch_toBuild import toBuild_tab

root_tabs = [[
				sg.Column([
					[
						sg.Text(text = "Current XP:"), sg.Input(default_text = "0", enable_events = True, justification = "right", size = (11, 1), key = "currentXpInput")
					],
					[
						sg.Text(text = "Current Level:"), sg.Input(default_text = "0", enable_events = True, justification = "right", size = (11, 1), key = "currentLevelInput")
					],
					[
						sg.Text(text = "Target XP:"), sg.Input(default_text = "0", enable_events = True, justification = "right", size = (11, 1), key = "targetXpInput")
					],
					[
						sg.Text(text = "Target Level:"), sg.Input(default_text = "0", enable_events = True, justification = "right", size = (11, 1), key = "targetLevelInput")
					],
					[
						sg.Text(text = "Outfit Pieces:"), sg.Combo(default_value = 0, values = [0, 1, 2, 3, 4, 5], enable_events = True, readonly = True, key = "outfitCombo")
					],
					[
						sg.Text(text = "2% Relic?"), sg.Checkbox(text = "", enable_events = True, key = "relicCheck")
					],
					[
						sg.Text(text = "Consider Artefacts"), sg.Checkbox(text = "", enable_events = True, key = "artefactCheck")
					],
					[
						sg.Text(text = "Purchase Materials?"), sg.Checkbox(text = "", enable_events = True, key = "materialCheck")
					],
					[
						sg.Text(text = "Prioritize"), sg.Combo(default_value = "Experience", values = ["Experience", "Compass Pieces", "Chronotes"], enable_events = True, readonly = True, key = "priorityCombo")
					],
					[
						sg.Button(button_text = "Save to File", enable_events = True, key = "saveFileButton"), #popup to confirm
						sg.Button(button_text = "Reset to Default", enable_events = True, key = "resetDefaultButton") # popup to configrm
					],
					[
						sg.Button(button_text = "Run Calculator", enable_events = True, key = "runCalculatorButton")
					]
				], element_justification = "center"),
				sg.Column([[
					sg.TabGroup(
					[[
						sg.Tab("Collections", collections_tab),
						sg.Tab("Materials", materials_tab),
						sg.Tab("Artefacts", artefacts_tab),
						sg.Tab("To Buy", toBuy_tab),
						sg.Tab("To Build", toBuild_tab)
					]])
				]])
			]]

window = sg.Window("RuneScape Archaeology Calculator", root_tabs)
window.Finalize()

# Event loop
while True:
	event, values = window.read(timeout = 120)

	if event == sg.WIN_CLOSED:
		break

	try:
		if event == "currentXpInput":
			if int(window["currentXpInput"].get()) > 200000000:
				window["currentXpInput"].update("200000000")
			window["currentLevelInput"].update(RsA_f.find_level(int(window["currentXpInput"].get())))

		elif event == "targetXpInput":
			if int(window["targetXpInput"].get()) > 200000000:
				window["targetXpInput"].update("200000000")
			window["targetLevelInput"].update(RsA_f.find_level(int(window["targetXpInput"].get())))
		
		elif event == "currentLevelInput":
			if int(window["currentLevelInput"].get()) > 120:
				window["currentLevelInput"].update("120")
			window["currentXpInput"].update(RsA_f.find_experience(int(window["currentLevelInput"].get())))
		
		elif event == "targetLevelInput":
			if int(window["targetLevelInput"].get()) > 120:
				window["targetLevelInput"].update("120")
			window["targetXpInput"].update(RsA_f.find_experience(int(window["targetLevelInput"].get())))

	except:
		window["currentXpInput"].update("0")
		window["currentLevelInput"].update("0")
		window["targetXpInput"].update("0")
		window["targetLevelInput"].update("0")

	if event != '__TIMEOUT__':
		print(event)

window.close()