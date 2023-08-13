import PySimpleGUI as sg

#RsLevels files
import RsLevels_skillWindow as RSL_skills
import RsLevels_functions as RSL_f

def launchLevelTracker():

	skillWindow = RSL_skills.SkillWindow()

	root_window = [[sg.Button("Update Stats")], [skillWindow.skill_frame]]
	window = sg.Window("RuneScape Level Caluclator", root_window)
	window.Finalize()

	while(1):
		event, values = window.read(timeout = 120)
		if event == sg.WIN_CLOSED:
			break

	RSL_f.save_skills()
	window.close()