import PySimpleGUI as sg

import RsLevels_functions as RSL_f

class SkillWindow:
	def __init__(self):
		self.skill_frame = self.create_skill_frame()

	def update_widgets(self, window, event, values):
		return

	def create_skill_frame(self):
		skill_layout = []
		for i in range(0, round(len(RSL_f.skill_order)/3)):
			skill_row = []
			for j in range(0, 3):
				skill_row.append(self.create_skill_icon(RSL_f.skill_order[3*i+j]))
			skill_layout.append(skill_row)
		return sg.Frame(layout = skill_layout, title = "Skills")

	def create_skill_icon(self, skill_name):
		return sg.Image(data = RSL_f.generate_image(f"images/{skill_name}.png", (26, 26)), tooltip = RSL_f.skill_dict[skill_name])