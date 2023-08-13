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

root_window = 	[
					[
						sg.Image(data = generate_image("images/Coins_10000.png", (32, 32))),
						sg.Text(text = "Price Checker"),
						sg.Button(button_text = "Launch", key = "launch_priceChecker")
					],
					[
						sg.Image(data = generate_image("images/Archaeology.png", (32, 32))),
						sg.Text(text = "Archaeology Calculator"),
						sg.Button(button_text = "Launch", key = "launch_archCalc")
					],
					[
						sg.Image(data = generate_image("images/Overall.png", (32, 32))),
						sg.Text(text = "Level Tracker"),
						sg.Button(button_text = "Launch", key = "launch_levelTracker")
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
window.close()