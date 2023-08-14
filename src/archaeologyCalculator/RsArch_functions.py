#####################################################
# RsArch_functions.py							    #
# Various functions and variables used by the		#
# Archaeology Calculator tool						#
#####################################################

import os
import io
import bisect
import json
import PySimpleGUI as sg
from PIL import Image, ImageDraw

import generalFunctions as func

# array of XP required to level up skills
level_xp = [0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363, 14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224, 41171, 45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333, 111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742, 302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627, 814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808, 1986068, 2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431, 14391160, 15889109, 17542976, 19368992, 21385073, 23611006, 26068632, 28782069, 31777943, 35085654, 38737661, 42769801, 47221641, 52136869, 57563718, 63555443, 70170840, 77474828, 85539082, 94442737, 104273167]

# array of active collections
active_collections = []

# Dictionary for archaeology data
arch_dict = func.load_json("data/arch_data.json", False)

# attempts to read a value from a dictionary, returning NaN on failure and sending an error message in the terminal
def read_value(dict, dict_path):
	try:
		if len(dict_path) == 0:
			return dict
		else:
			return read_value(dict[dict_path[0]], dict_path[1:])
	except:
		print(f"WARN: invalid dictionary path: {dict_path}")
		return "NaN"

# determines the default collections to consider based on preference and level
def determine_collections(preference, level):
	return

# Determines which artefacts to build based on input parameters
def determine_artefacts(collections_only, priority):
	if priority == "Experience" and not collections_only:
		# Single Artefacts
		return
	else:
		# Collections
		return