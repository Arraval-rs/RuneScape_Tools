import PySimpleGUI as sg

#RsLevels files
import RsLevels_skillWindow as RSL_skills
import RsLevels_functions as RSL_f

def launchLevelTracker():

	skillWindow = RSL_skills.SkillWindow()

	root_window = [[sg.Button("Update Stats"), sg.Input(size = (12, 1), enable_events = True, key = "player_name"), sg.Text(f"Player: {RSL_f.skill_dict['player_name'] if 'player_name' in RSL_f.skill_dict else 'None'}", key = "current_player")], skillWindow.format_window()]
	window = sg.Window("RuneScape Level Calculator", root_window)
	window.Finalize()

	while(1):
		event, values = window.read(timeout = 120)
		if event == sg.WIN_CLOSED:
			break
		if event == "player_name" and len(values["player_name"]) > 12:
			window["player_name"].update(values["player_name"][0:12])
		else:
			skillWindow.update_widgets(window, event, values)
		if event != "__TIMEOUT__":
			print(f"Event: {event}\nValues: {values}")
	RSL_f.save_skills()
	window.close()
	return False