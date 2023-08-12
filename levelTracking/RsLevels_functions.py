import os, io, json
from PIL import Image, ImageDraw

import RsLevels_skill as RSL_skills

def load_skills():
	try:
		# change data parse to creating items
		json_file = open("data/skills.json", "rt")
		data = json.loads(json_file.read())
		for skill in data:
			data[skill] = json_to_skill(data[skill])
		return data
	except:
		print("WARN: Cannot find data/skills.json")
		dict = {}
		for item in skill_order:
			dict[item] = RSL_skills.Skill(item, 0, 0, 0, 0, 0)
		print(dict)
		return dict

def save_skills():
	for skill in skill_dict:
		skill_dict[skill] = skill_to_json(skill_dict[skill])
	output_file = open("data/skills.json", "w")
	json.dump(skill_dict, output_file)
	return

def query_skills():
	return

def skill_to_json(skill):
	return {"Name": skill.name, "Rank": skill.rank, "Current Level": skill.current_level, "Current Experience": skill.current_xp, "target Level": skill.target_level, "target Experience": skill.target_xp}

def json_to_skill(json):
	return RSL_skills.Skill(json["Name"], json["Rank"], json["Current Level"], json["Current Experience"], json["target Level"], json["Current Experience"])

def generate_image(file, size):
	if not os.path.exists(file):
		print(f'WARN: Cannot find{file}')
		file = 'images/Missing.png'
	img = Image.open(file).resize(size)
	bio = io.BytesIO()
	img.save(bio, format = "PNG")
	return bio.getvalue()

skill_order = ["Overall", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction", "Summoning", "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"]
#activity_order = [Bounty Hunter, B.H. Rogues, Dominion Tower, The Crucible, Castle Wars games, B.A. Attackers, B.A. Defenders, B.A. #Collectors, B.A. Healers, Duel Tournament, Mobilising Armies, Conquest, Fist of Guthix, GG: Athletics, GG: Resource #Race, WE2: Armadyl Lifetime Contribution, WE2: Bandos Lifetime Contribution, WE2: Armadyl PvP kills, WE2: Bandos PvP #kills, Heist Guard Level, Heist Robber Level, CFP: 5 game average, AF15: Cow Tipping, AF15: Rats killed after the #miniquest, RuneScore, Clue Scrolls Easy, Clue Scrolls Medium, Clue Scrolls Hard, Clue Scrolls Elite, Clue Scrolls Master]

skill_dict = load_skills()
#Other Images:
#https://runescape.wiki/w/Category:Detailed_skill_icons