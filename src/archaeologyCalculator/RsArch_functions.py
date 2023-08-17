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
import RsArch_collection as RsA_coll
import RsArch_artefact as RsA_art

# attempts to read a value from a dictionary, returning NaN on failure and printing an error message to terminal
def read_value(dict, dict_path):
	try:
		if len(dict_path) == 0:
			return dict
		else:
			value = read_value(dict[dict_path[0]], dict_path[1:])
			if value == "NaN":
				print(f"\tERROR: Continued path: {dict_path}")
			return value
	except:
		print(f"ERROR: invalid dictionary path: {dict_path}")
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

def create_artefacts(data):
	arts = {}
	for faction in data["Artefacts"]:
		faction_artefacts = []
		for key in list(data["Artefacts"][faction]):
			try:
				artefact = RsA_art.Artefact(key, data["Artefacts"][faction][key])
				faction_artefacts.append(artefact)
			except Exception as e:
				print(f"WARN: Could not create Artefact with exception:\n\tWARN: {e}")
				try:
					print(f"\tData read: {data['Artefacts'][faction][key]}")
				except:
					print("\tERROR: No data read!")
		arts[faction] = faction_artefacts
	return arts
	return arts

def create_materials(data):
	mats = []
	return mats

def create_collections(data):
	colls = {}
	for faction in data["Collections"]:
		faction_collections = []
		for i in range(0, len(data["Collections"][faction])):
			try:
				collection = RsA_coll.Collection(data["Collections"][faction][i])
				faction_collections.append(collection)
			except Exception as e:
				print(f"WARN: Could not create Collection with exception:\n\tWARN: {e}")
				try:
					print(f"\tData read: {data['Collections'][faction][i]}")
				except:
					print("\tERROR: No data read!")
		colls[faction] = faction_collections
	return colls

def save_arch_data():
	print(f"\tArtefacts: {len(artefacts)}\n\tMaterials: {len(materials)}\n\tCollections: {len(collections)}")
	return

# Dictionary for archaeology data
arch_dict = func.load_json("data/arch_data.json", False)

# List of Artefact objects imported from json
artefacts = create_artefacts(arch_dict)

# List of Material objects imported from json
materials = create_materials(arch_dict)

# List of Collection objects imported from json
collections = create_collections(arch_dict)