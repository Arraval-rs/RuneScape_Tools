import os, io, re, json
import urllib.request
from bisect import bisect_left
from PIL import Image, ImageDraw

import RsLevels_skill as RSL_skills

# load saved skills stats from file (data/skills.json)
def load_skills():
	try:
		# change data parse to creating items
		json_file = open("data/skills.json", "rt")
		data = json.loads(json_file.read())
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
	output_file = open("data/skills.json", "w")
	json.dump(save_dict, output_file)
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

# generate image from file of given size
def generate_image(file, size):
	if not os.path.exists(file):
		print(f'WARN: Cannot find{file}')
		file = 'images/Missing.png'
	img = Image.open(file).resize(size)
	bio = io.BytesIO()
	img.save(bio, format = "PNG")
	return bio.getvalue()

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

# validates numerical input to limit value between (1, max_value) and remove non-numerics
def validate_numeric(number, max_value):
	result = re.sub("[^0-9]", "", number)
	if result == "":
		result = 1
	return max(1, min(int(result), max_value))

# returns experience required for input level
def find_experience(level, elite):
	if elite:
		return elite_experience_values[level - 1]
	return experience_values[level - 1]

# returns level attained by input experience 
def find_level(experience, elite):
	if elite:
		return bisect_left(elite_experience_values, experience)
	return bisect_left(experience_values, experience)


# Order of skill data parsed from hiscores
skill_order = ["Overall", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction", "Summoning", "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"]
#activity_order = [Bounty Hunter, B.H. Rogues, Dominion Tower, The Crucible, Castle Wars games, B.A. Attackers, B.A. Defenders, B.A. #Collectors, B.A. Healers, Duel Tournament, Mobilising Armies, Conquest, Fist of Guthix, GG: Athletics, GG: Resource #Race, WE2: Armadyl Lifetime Contribution, WE2: Bandos Lifetime Contribution, WE2: Armadyl PvP kills, WE2: Bandos PvP #kills, Heist Guard Level, Heist Robber Level, CFP: 5 game average, AF15: Cow Tipping, AF15: Rats killed after the #miniquest, RuneScore, Clue Scrolls Easy, Clue Scrolls Medium, Clue Scrolls Hard, Clue Scrolls Elite, Clue Scrolls Master]

# dictionary of all skill objects
skill_dict = load_skills()

# currently selected skill object
selected_skill = skill_dict["Attack"]

# List of experience required for each level in standard skills
experience_values = [0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363, 14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224, 41171, 45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333, 111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742, 302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627, 814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808, 1986068, 2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431, 14391160, 15889109, 17542976, 19368992, 21385073, 23611006, 26068632, 28782069, 31777943, 35085654, 38737661, 42769801, 47221641, 52136869, 57563718, 63555443, 70170840, 77474828, 85539082, 94442737, 104273167]

# List of experience required for each level in elite skills
elite_experience_values = [0, 830, 1861, 2902, 3980, 5126, 6390, 7787, 9400, 11275, 13605, 16372, 19656, 23546, 28138, 33520, 39809, 47109, 55535, 64802, 77190, 90811, 106221, 123573, 143025, 164742, 188893, 215651, 245196, 277713, 316311, 358547, 404634, 454796, 509259, 568254, 632019, 700797, 748834, 854383, 946227, 1044569, 1149696, 1261903, 1381488, 1508756, 1644015, 1787581, 1939773, 2100917, 2283490, 2476369, 2679907, 2894505, 3120508, 3358307, 3608290, 3870846, 4146374, 4435275, 4758122, 5096111, 5449685, 5819299, 6205407, 6608473, 7028964, 7467354, 7924122, 8399751, 8925664, 9472665, 10041285, 10632061, 11245538, 11882262, 12542789, 13227679, 13937496, 14672812, 15478994, 16313404, 17176661, 18069395, 18992239, 19945833, 20930821, 21947856, 22997593, 24080695, 25259906, 26475754, 27728955, 29020233, 30350318, 31719944, 33129852, 34580790, 36073511, 37608773, 39270442, 40978509, 42733789, 44537107, 46389292, 48291180, 50243611, 52247435, 54303504, 56412678, 58575823, 60793812, 63067521, 65397835, 67785643, 70231841, 72737330, 75303019, 77929820, 80618654, 83370445, 86186124, 89066630, 92012904, 95025896, 98106559, 101255855, 104474750, 107764216, 111125230, 114558777, 118065845, 121647430, 125304532, 129038159, 132849323, 136739041, 140708338, 144758242, 148889790, 153104021, 157401983, 161784728, 166253312, 170808801, 175452262, 180184770, 185007406, 189921255, 194927409]