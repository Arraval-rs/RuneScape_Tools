#####################################################
# RsLevels_skillWindow.py							#
# Skill summary elements and functions				#
#####################################################

import PySimpleGUI as sg

import generalFunctions as func
import RsLevels_functions as RSL_f

class SkillWindow:
	def __init__(self):
		self.skill_frame = self.create_skill_frame()
		self.stat_frame = self.create_stat_frame()
		self.overall_frame = self.create_overall_frame()
		self.combat_frame = self.create_combat_frame()

	def update_widgets(self, window, event, values):
		if event == "Update Stats" and len(values["player_name"]) > 0:
			if RSL_f.query_skills(values["player_name"]):
				window["current_player"].update(f"Player: {values['player_name']}")
			self.update_skill_stats(RSL_f.selected_skill.name, window)
			self.update_overall_stats(window)
			self.update_combat_levels(window)
		elif "Icon" in event and "Overall" not in event:
			RSL_f.selected_skill = RSL_f.skill_dict[event.split()[0]]
			self.update_skill_stats(RSL_f.selected_skill.name, window)
		elif "skill_level_input" == event:
			level = func.validate_numeric(values['skill_level_input'], 120)
			window["skill_level_input"].update(f"{level:,}")
			RSL_f.selected_skill.target_level = level
			RSL_f.selected_skill.target_xp = func.find_experience(level, RSL_f.selected_skill.name == "Invention")
			window["skill_xp_input"].update(f"{RSL_f.selected_skill.target_xp:,}")
			window["skill_remainder"].update(f"Remainder: {max(0, int(RSL_f.selected_skill.target_xp) - int(RSL_f.selected_skill.current_xp)):,}")
		elif "skill_xp_input" == event:
			experience = func.validate_numeric(values['skill_xp_input'], 200000000)
			window["skill_xp_input"].update(f"{experience:,}")
			RSL_f.selected_skill.target_xp = experience
			RSL_f.selected_skill.target_level = func.find_level(experience, RSL_f.selected_skill.name == "Invention")
			window["skill_level_input"].update(f"{RSL_f.selected_skill.target_level:,}")
			window["skill_remainder"].update(f"Remainder: {max(0, int(RSL_f.selected_skill.target_xp) - int(RSL_f.selected_skill.current_xp)):,}")
		elif "overall_xp_input" == event:
			RSL_f.skill_dict["Overall"].target_xp = func.validate_numeric(values['overall_xp_input'], 5600000000)
			window["overall_xp_input"].update(f"{RSL_f.skill_dict['Overall'].target_xp:,}")
			window["overall_remainder"].update(f"Remainder: {max(0, int(RSL_f.skill_dict['Overall'].target_xp) - int(RSL_f.skill_dict['Overall'].current_xp)):,}")
		return

	def update_skill_stats(self, skill_name, window):
		window["skill_rank"].update(f"Name:  {RSL_f.skill_dict[skill_name].name}\nRank: {int(RSL_f.skill_dict[skill_name].rank):,}\nLevel:  {int(RSL_f.skill_dict[skill_name].current_level):,}\nCurrent XP:  {int(RSL_f.skill_dict[skill_name].current_xp):,}\nNext Level:  {0}")
		window["skill_level_input"].update(f"{int(RSL_f.skill_dict[skill_name].target_level):,}")
		window["skill_xp_input"].update(f"{int(RSL_f.skill_dict[skill_name].target_xp):,}")
		window["skill_remainder"].update(f"Remainder: {max(0, int(RSL_f.skill_dict[skill_name].target_xp) - int(RSL_f.skill_dict[skill_name].current_xp)):,}")

	def update_overall_stats(self, window):
		window["overall_rank"].update(f"Rank:  {int(RSL_f.skill_dict['Overall'].rank):,}\nTotal Level:  {int(RSL_f.skill_dict['Overall'].current_level):,}\nTotal XP:  {int(RSL_f.skill_dict['Overall'].current_xp):,}")
		window["overall_xp_input"].update(f"{int(RSL_f.skill_dict['Overall'].target_xp):,}")
		window["overall_remainder"].update(f"Remainder:  {max(0, int(RSL_f.skill_dict['Overall'].target_xp) - int(RSL_f.skill_dict['Overall'].current_xp)):,}")

	def update_combat_levels(self, window):
		window["combat_levels"].update(f"Melee: {RSL_f.calculate_combat_level('Melee')}\nRanged: {RSL_f.calculate_combat_level('Ranged')}\nMagic: {RSL_f.calculate_combat_level('Magic')}\nNecromancy:{RSL_f.calculate_combat_level('Necromancy')}")

	def format_window(self):
		return [self.skill_frame, sg.Column(layout = [[self.stat_frame],[self.overall_frame], [self.combat_frame]])]

	def create_skill_frame(self):
		skill_layout = []
		for i in range(0, round(len(RSL_f.skill_order)/3)):
			skill_row = []
			for j in range(0, 3):
				skill_row.append(self.create_skill_icon(RSL_f.skill_order[3*i+j]))
			skill_layout.append(skill_row)
		return sg.Frame(layout = skill_layout, title = "Skills")

	def create_skill_icon(self, skill_name):
		return sg.Image(data = func.generate_image(f"images/{skill_name}.png", (26, 26), True), tooltip = skill_name, enable_events = True, key = f"{skill_name} Icon")

	def create_stat_frame(self):
		stat_layout =	[
							[
								sg.Text(f"Name:  {RSL_f.skill_dict['Attack'].name}\nRank: {int(RSL_f.skill_dict['Attack'].rank):,}\nLevel:  {int(RSL_f.skill_dict['Attack'].current_level):,}\nCurrent XP:  {int(RSL_f.skill_dict['Attack'].current_xp):,}\nNext Level:  {0}", key = "skill_rank"),
							],
							[
								sg.Text("Target Level:"),
								sg.Input(default_text = f"{int(RSL_f.skill_dict['Attack'].target_level):,}", size = (3, 1), enable_events = True, key = "skill_level_input")
							],
							[
								sg.Text("Target XP:"),
								sg.Input(default_text = f"{int(RSL_f.skill_dict['Attack'].target_xp):,}", size = (11, 1), enable_events = True, key = "skill_xp_input")
							],
							[
								sg.Text(f"Remainder: {max(0, int(RSL_f.skill_dict['Attack'].target_xp) - int(RSL_f.skill_dict['Attack'].current_xp)):,}", key = "skill_remainder")
							]
						]
		return sg.Frame(layout = stat_layout, title = "Skill Stats")	

	def create_overall_frame(self):
		overall_layout =	[
								[
									sg.Text(f"Rank:  {int(RSL_f.skill_dict['Overall'].rank):,}\nTotal Level:  {int(RSL_f.skill_dict['Overall'].current_level):,}\nTotal XP:  {int(RSL_f.skill_dict['Overall'].current_xp):,}", key = "overall_rank")
								],
								[
									sg.Text("Target XP:"),
									sg.Input(default_text = f"{int(RSL_f.skill_dict['Overall'].target_xp):,}",size= (13, 1), enable_events = True, key = "overall_xp_input")
								],
								[
									sg.Text(f"Remainder:  {max(0, int(RSL_f.skill_dict['Overall'].target_xp) - int(RSL_f.skill_dict['Overall'].current_xp)):,}", key = "overall_remainder")
								]
							]
		return sg.Frame(layout = overall_layout, title = "Overall Stats")	

	def create_combat_frame(self):
		combat_layout = 	[
								[
									sg.Text(f"Melee:  {RSL_f.calculate_combat_level('Melee')}\nRanged:  {RSL_f.calculate_combat_level('Ranged')}\nMagic:  {RSL_f.calculate_combat_level('Magic')}\nNecromancy:  {RSL_f.calculate_combat_level('Necromancy')}", key = "combat_levels")
								]
							]
		return sg.Frame(layout = combat_layout, title = "Combat Levels")