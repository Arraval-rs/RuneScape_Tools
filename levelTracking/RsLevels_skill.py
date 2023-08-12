class Skill:
	def __init__(self, name, rank, level, xp, target_level, target_xp):
		self.name = name
		self.rank = rank
		self.current_level = level
		self.current_xp = xp
		self.target_level = target_level
		self.target_xp = target_xp
		return

	def __str__(self):
		return	(f"{self.name}: {self.current_level}\n" +
				f"Current XP: {self.current_xp}\n"+
				f"Next Level: \n" +
				f"Target lvl: {self.target_level}\n" +
				f"Target XP: {self.target_xp}\n" +
				f"Remainder:")