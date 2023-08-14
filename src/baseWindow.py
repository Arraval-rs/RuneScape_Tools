import PySimpleGUI as sg
from PIL import Image, ImageDraw
import sys, os, io

sys.path.append(os.path.basename("levelTracking"))
sys.path.append(os.path.basename("archaeologyCalculator"))
sys.path.append(os.path.basename("priceChecker"))

# RS Tool Files
import RsLevels_main as RSLevel
import RsArch_main as RSArch
import RSGE_main as RSPrice

def generate_image(file, size):
	img = Image.open(file).resize(size)
	bio = io.BytesIO()
	img.save(bio, format = "PNG")
	return bio.getvalue()

text_spacing = 12
button_spacing = 6

root_window = 	[
					[sg.Column(layout = [
											[sg.Image(data = generate_image("images/Coins_10000.png", (32, 32)))],
											[sg.Image(data = generate_image("images/Archaeology.png", (32, 32)))],
											[sg.Image(data = generate_image("images/Overall.png", (32, 32)))]
					]),
					sg.Column(layout = [
											[sg.Text(text = "Price Checker")],
											[sg.Sizer(0, text_spacing)],
											[sg.Text(text = "Archaeology Calculator")],
											[sg.Sizer(0, text_spacing)],
											[sg.Text(text = "Level Tracker")]
					]),
					sg.Column(layout = [
											[sg.Button(button_text = "Launch", key = "launch_priceChecker")],
											[sg.Sizer(0, button_spacing)],
											[sg.Button(button_text = "Launch", key = "launch_archCalc")],
											[sg.Sizer(0, button_spacing)],
											[sg.Button(button_text = "Launch", key = "launch_levelTracker")]
										])
					]
				]

window = sg.Window("RuneScape Tools", root_window)

while(1):
	event, values = window.read(timeout = 120)
	if event == sg.WIN_CLOSED:
		break
	if event == "launch_levelTracker":
		RSLevel.launchLevelTracker()
	elif event == "launch_archCalc":
		RSArch.launchArchCalc()
	elif event == "launch_priceChecker":
		RSPrice.launchPriceChecker()
	# if event != "__TIMEOUT__":
	# 	print(f"Event: {event}\nValues: {values}")
window.close()