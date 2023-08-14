#####################################################
# RsLevels_functions.py                             #
# Various functions and variables used by the		#
# Level Tracker	tool								#
#####################################################

import os, io, re, json
import urllib.request
from bisect import bisect_left
from PIL import Image, ImageDraw

import generalFunctions as func
import RsLevels_skill as RSL_skills

# load saved skills stats from file (data/skills.json)
def load_skills():
	try:
		data = func.load_json("data/skills.json", False)
		for skill in data:
			if skill != "player_name":
				data[skill] = json_to_skill(data[skill])
		return data
	except Exception as e:
		print(f"WARN: Cannot load data/skills.json\n\tWARN: {e}")
		dict = {}
		for item in skill_order:
			dict[item] = RSL_skills.Skill(item, 0, 0, 0, 0, 0)
		return dict

# save skill stats to file (data/skills.json)
def save_skills():
	save_dict = {}
	for skill in skill_dict:
		if skill != "player_name":
			save_dict[skill] = skill_to_json(skill_dict[skill])
		else:
			save_dict[skill] = skill_dict[skill]
	func.save_json(save_dict, "data/skills.json")
	return

# update skill stats from highscores (https://secure.runescape.com/m=hiscore/index_lite.ws?player=<name>)
def query_skills(name):
	try:
		url = f"https://secure.runescape.com/m=hiscore/index_lite.ws?player={name}"
		request = urllib.request.Request(url, headers = {"User-Agent" : "Magic Browser"})
		content = urllib.request.urlopen(request)
		data = content.read().decode().split("\n")
		iter = 0
		for entry in data:
			values = entry.split(",")
			if len(values) > 2:
				skill_dict[skill_order[iter]].rank = values[0]
				skill_dict[skill_order[iter]].current_level = values[1]
				skill_dict[skill_order[iter]].current_xp = values[2]
				iter += 1
		skill_dict["player_name"] = name
		return True
	except Exception as e:
		print(f"WARN: Could not query {url}\n\tWARN: {e}") # error popup?
		return False

# convert skill object to json parseable content
def skill_to_json(skill):
	return {"Name": skill.name, "Rank": skill.rank, "Current Level": skill.current_level, "Current Experience": skill.current_xp, "target Level": skill.target_level, "target Experience": skill.target_xp}

# convert json parseable content to skill object
def json_to_skill(json):
	return RSL_skills.Skill(json["Name"], json["Rank"], json["Current Level"], json["Current Experience"], json["target Level"], json["Current Experience"])

# calculate combat level of given style
def calculate_combat_level(style):
	defence = int(skill_dict["Defence"].current_level)
	constitution = int(skill_dict["Constitution"].current_level)
	prayer = int(int(skill_dict["Prayer"].current_level) / 2)
	summoning = int(int(skill_dict["Summoning"].current_level) / 2)
	if style == "Melee":
		melee = int(skill_dict["Attack"].current_level) + int(skill_dict["Strength"].current_level)
		return int(((13/10) * melee + defence + constitution + prayer + summoning) / 4)
	return int(((13/5) * int(skill_dict[style].current_level) + defence + constitution + prayer + summoning) / 4)

# Order of skill data parsed from hiscores
skill_order = ["Overall", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction", "Summoning", "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"]
#activity_order = [Bounty Hunter, B.H. Rogues, Dominion Tower, The Crucible, Castle Wars games, B.A. Attackers, B.A. Defenders, B.A. #Collectors, B.A. Healers, Duel Tournament, Mobilising Armies, Conquest, Fist of Guthix, GG: Athletics, GG: Resource #Race, WE2: Armadyl Lifetime Contribution, WE2: Bandos Lifetime Contribution, WE2: Armadyl PvP kills, WE2: Bandos PvP #kills, Heist Guard Level, Heist Robber Level, CFP: 5 game average, AF15: Cow Tipping, AF15: Rats killed after the #miniquest, RuneScore, Clue Scrolls Easy, Clue Scrolls Medium, Clue Scrolls Hard, Clue Scrolls Elite, Clue Scrolls Master]

# dictionary of all skill objects
skill_dict = load_skills()

# currently selected skill object
selected_skill = skill_dict["Attack"]

# dictionary of previous input box states
old = {
	"skill_level_input": 0,
	"skill_xp_input": 0,
	"overall_xp_input": 0
}