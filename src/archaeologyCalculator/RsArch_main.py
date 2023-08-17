#####################################################
# RsArch_main.py                                    #
# Event loop of the Archaeology Calculator tool		#
#####################################################

import os, io, json, psutil
import PySimpleGUI as sg

# RsArch files
import RsArch_functions as RsA_f
import RsArch_collectionTab as RSA_coll
import RsArch_materialTab as RSA_mats
import RsArch_artefactTab as RSA_art
import RsArch_toBuy as RSA_buy
import RsArch_toBuild as RSA_build
import generalFunctions as func

class ArchaeologyCalculator:
	def __init__(self):
		self.collections = RSA_coll.CollectionTab()
		self.materials = RSA_mats.MaterialTab()
		self.artefacts = RSA_art.ArtefactTab()
		self.toBuy = RSA_buy.ToBuyTab()
		self.toBuild = RSA_build.ToBuildTab()
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
								sg.Text(text = "Prioritize"), sg.Combo(default_value = "Experience", values = ["Experience", "Compass Pieces", "Chronotes", "Profit"], enable_events = True, readonly = True, key = "priorityCombo")
							],
							[
								sg.Button(button_text = "Save to File", enable_events = True), # popup to confirm
								sg.Button(button_text = "Reset to Default", enable_events = True) # popup to confirm
							],
							[
								sg.Button(button_text = "Run Calculator", enable_events = True)
							]
						], element_justification = "center"),
						sg.Column([[
							sg.TabGroup(
							[[
								sg.Tab("Collections", self.collections.layout),
								sg.Tab("Materials", self.materials.layout),
								sg.Tab("Artefacts", self.artefacts.layout),
								sg.Tab("To Buy", self.toBuy.layout),
								sg.Tab("To Build", self.toBuild.layout)
							]])
						]])
					]]
		self.window = sg.Window("RuneScape Archaeology Calculator", root_tabs)
		self.window.Finalize()

	def eventLoop(self):
		window = self.window
		# Event loop
		while True:
			event, values = window.read(timeout = 120)
			if event == sg.WIN_CLOSED:
				break
			if event == "currentXpInput":
				window["currentXpInput"].update(f"{func.validate_numeric(window['currentXpInput'].get(), 200000000):,}")
				current_level = func.find_level(func.validate_numeric(window['currentXpInput'].get(), 200000000), False)
				window["currentLevelInput"].update(f"{current_level:,}")
			elif event == "currentLevelInput":
				window["currentLevelInput"].update(f"{func.validate_numeric(window['currentLevelInput'].get(), 120):,}")
				current_xp = func.find_experience(int(window['currentLevelInput'].get()), False)
				window["currentXpInput"].update(f"{current_xp:,}")
			elif event == "targetXpInput":
				window["targetXpInput"].update(f"{func.validate_numeric(window['targetXpInput'].get(), 200000000):,}")
				current_level = func.find_level(func.validate_numeric(window['targetXpInput'].get(), 200000000), False)
				window["targetLevelInput"].update(f"{current_level:,}")
			elif event == "targetLevelInput":
				window["targetLevelInput"].update(f"{func.validate_numeric(window['targetLevelInput'].get(), 120):,}")
				current_xp = func.find_experience(int(window['targetLevelInput'].get()), False)
				window["targetXpInput"].update(f"{current_xp:,}")
			elif event == "Save to File":
				save_dict = RsA_f.save_arch_data()
			elif event != "__TIMEOUT__":
				self.materials.material_events(window, event)
				self.artefacts.artefact_events(window, event)
			if event != '__TIMEOUT__':
				print(f"Event: {event}")
				#print(f"Values: {values}")
			else: #Performance Check
				print(f"\n\t\tRAM: {psutil.virtual_memory()[2]}% ({psutil.virtual_memory()[3]/1000000000} GB)\n")
		window.close()