#####################################################
# RsArch_artefact.py                                #
# Artefact objects used to hold various data        #
#####################################################

class Artefact:
	def __init__(self, name, data):
		self.name = name
		self.level = data["Level"]
		self.stored = data["Stored"]
		self.xp = data["Experience"]
		self.materials = data["Materials"]
		return

	def __str__(self):
		return ""