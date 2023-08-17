#####################################################
# generalFunctions.py							    #
# Various functions and variables used across 		#
# multiple tools									#
#####################################################

import os, io, re, json
import urllib.request
from bisect import bisect_left
from PIL import Image, ImageDraw

# generates an image with the given file and size. Optionally generates a background square
# Will attempt to retreive an already loaded image before generating a new one (Needs improvement)
def generate_image(f, s, bg):
	if "None" in f:
		f = 'images/Empty Slot.png'
	if not os.path.exists(f):
		print(f"WARN: Missing image '{f}'")
		f = 'images/Missing.png'
	if f"{f}_{s}_{bg}" in loaded_images:
		return loaded_images[f"{f}_{s}_{bg}"]
	img = Image.open(f).resize(s)
	if bg:
		item_bg = Image.open('images/Empty Slot.png').resize(s)
		item_bg.paste(img, (0, 0), img.convert('RGBA'))
		img = item_bg
	img.thumbnail(s)
	bio = io.BytesIO()
	img.save(bio, format = "PNG")
	loaded_images[f"{f}_{s}_{bg}"] = bio.getvalue()
	return loaded_images[f"{f}_{s}_{bg}"]

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

# Generates a dictionary from json read from the given source
# Compatible with websites containing json data with the isUrl flag
def load_json(source, isUrl):
	try:
		if(isUrl):
			request = urllib.request.Request(source, headers={"User-Agent" : "Magic Browser"})
			content = urllib.request.urlopen(request)
			return json.loads(content.read())
		json_file = open(source, "rt")
		data = json.loads(json_file.read())
		return data
	except Exception as e:
		print(f"WARN: Cannot load from {source} with the following exception:\n\tWARN: {e}")
		return {}

# load save input values to json at specified path
def save_json(data, path):
	try:
		output_file = open(path, "w")
		json.dump(data, output_file)
	except Exception as e:
		print(f"WARN: Cannot write to {path} with the following exception:\n\tWARN: {e}")

# validates numerical input to limit value between (1, max_value) and remove non-numerics
def validate_numeric(number, max_value):
	result = re.sub("[^0-9]", "", number)
	if result == "":
		result = 1
	return max(1, min(int(result), max_value))

# List of experience required for each level in standard skills
experience_values = [0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363, 14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224, 41171, 45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333, 111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742, 302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627, 814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808, 1986068, 2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431, 14391160, 15889109, 17542976, 19368992, 21385073, 23611006, 26068632, 28782069, 31777943, 35085654, 38737661, 42769801, 47221641, 52136869, 57563718, 63555443, 70170840, 77474828, 85539082, 94442737, 104273167]

# List of experience required for each level in elite skills
elite_experience_values = [0, 830, 1861, 2902, 3980, 5126, 6390, 7787, 9400, 11275, 13605, 16372, 19656, 23546, 28138, 33520, 39809, 47109, 55535, 64802, 77190, 90811, 106221, 123573, 143025, 164742, 188893, 215651, 245196, 277713, 316311, 358547, 404634, 454796, 509259, 568254, 632019, 700797, 748834, 854383, 946227, 1044569, 1149696, 1261903, 1381488, 1508756, 1644015, 1787581, 1939773, 2100917, 2283490, 2476369, 2679907, 2894505, 3120508, 3358307, 3608290, 3870846, 4146374, 4435275, 4758122, 5096111, 5449685, 5819299, 6205407, 6608473, 7028964, 7467354, 7924122, 8399751, 8925664, 9472665, 10041285, 10632061, 11245538, 11882262, 12542789, 13227679, 13937496, 14672812, 15478994, 16313404, 17176661, 18069395, 18992239, 19945833, 20930821, 21947856, 22997593, 24080695, 25259906, 26475754, 27728955, 29020233, 30350318, 31719944, 33129852, 34580790, 36073511, 37608773, 39270442, 40978509, 42733789, 44537107, 46389292, 48291180, 50243611, 52247435, 54303504, 56412678, 58575823, 60793812, 63067521, 65397835, 67785643, 70231841, 72737330, 75303019, 77929820, 80618654, 83370445, 86186124, 89066630, 92012904, 95025896, 98106559, 101255855, 104474750, 107764216, 111125230, 114558777, 118065845, 121647430, 125304532, 129038159, 132849323, 136739041, 140708338, 144758242, 148889790, 153104021, 157401983, 161784728, 166253312, 170808801, 175452262, 180184770, 185007406, 189921255, 194927409]

# Dict of loaded images to retreive from
loaded_images = {}