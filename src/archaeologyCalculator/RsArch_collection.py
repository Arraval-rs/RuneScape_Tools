#####################################################
# RsArch_collection.py                              #
# Collection objects used to hold various data      #
#####################################################
import RsArch_functions as RsA_f

class Collection:
	def __init__(self, json):
		self.name = json["Name"]
		self.level = json["Level"]
		self.xp = json["XP"]
		self.chronotes = json["Chronotes"]
		self.tetra = json["Tetra"]
		self.enabled = json["Enabled"]
		self.artefacts = json["Artefacts"]
		self.materials = self.determine_mats()

	def __str__(self):
		string =(
					f"\t{self.name}:" +
					f"\t\tLevel: {self.level}" +
					f"\t\tXP: {self.xp}" +
					f"\t\tChronotes: {self.chronotes}" +
					f"\t\tTetra?: {self.tetra}" +
					f"\t\tEnabled?: {self.enabled}" +
					f"\t\tArtefacts: {self.artefacts}" +
					f"\t\tMaterials: {self.materials}"
				)
		return string

	def determine_mats(self):
		mats = {}
		for artefact in self.artefacts:
			for faction in RsA_f.artefacts:
				for art in RsA_f.artefacts[faction]:
					if artefact == art.name:
						for material in art.materials:
							if material["Name"] in list(mats):
								mats[material["Name"]]["Count"] += material["Count"]
							else:
								mats[material["Name"]] = material
		return mats