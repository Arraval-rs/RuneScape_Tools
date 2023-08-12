import urllib.request

url = "https://secure.runescape.com/m=hiscore/index_lite.ws?player=Arraval"
request = urllib.request.Request(url, headers = {"User-Agent" : "Magic Browser"})
content = urllib.request.urlopen(request)
data = content.read().decode().split("\n")

dict = {}
iter = 0
skills = ["Overall", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction", "Summoning", "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"]

for entry in data:
	values = entry.split(",")
	if len(values) > 2:
		dict[skills[iter]] = {"Rank":values[0], "Level":values[1], "Experience": values[2]}
		iter += 1

print(dict)

#The skills in order are:

#Overall, Attack, Defence, Strength, Constitution, Ranged, Prayer, Magic, Cooking, Woodcutting, Fletching, Fishing, #Firemaking, Crafting, Smithing, Mining, Herblore, Agility, Thieving, Slayer, Farming, Runecrafting, Hunter, #Construction, Summoning, Dungeoneering, Divination, Invention, Archaeology.

#Followed by activities:

#Bounty Hunter, B.H. Rogues, Dominion Tower, The Crucible, Castle Wars games, B.A. Attackers, B.A. Defenders, B.A. #Collectors, B.A. Healers, Duel Tournament, Mobilising Armies, Conquest, Fist of Guthix, GG: Athletics, GG: Resource #Race, WE2: Armadyl Lifetime Contribution, WE2: Bandos Lifetime Contribution, WE2: Armadyl PvP kills, WE2: Bandos PvP #kills, Heist Guard Level, Heist Robber Level, CFP: 5 game average, AF15: Cow Tipping, AF15: Rats killed after the #miniquest, RuneScore, Clue Scrolls Easy, Clue Scrolls Medium, Clue Scrolls Hard, Clue Scrolls Elite, Clue Scrolls #Master