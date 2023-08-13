#####################################################
# RSGE_lookup.py                                    #
# Item Lookup elements and functions                #
#####################################################

import PySimpleGUI as sg
import RSGE_functions as RSGE_f
import RSGE_item

class LookupWindow:

	def __init__(self):
		self.lookup_frame = self.create_lookup_frame(self.create_lookup_item_frame())
		self.lookup_items = []
		self.lookup_ids = []

	# Updates all lookup elements when a related event occurs
	def update_widgets(self, window, event, values):

		# Search Button Event
		if event == "Search":
			if len(window["lookup_input"].get()) < 3:
				window["lookup_list"].update(["Search key too short"])
			else:
				self.lookup_items = []
				self.lookup_ids = []
				matches = 0
				match_string = window["lookup_input"].get()
				for item in RSGE_f.gazbot_dict:
					if "%" not in item:
						if match_string in RSGE_f.gazbot_dict[item]["name"]:
							self.lookup_items.append(RSGE_f.gazbot_dict[item]["name"])
							self.lookup_ids.append(RSGE_f.gazbot_dict[item]["id"])
				if len(self.lookup_items) < 1:
					window["lookup_list"].update(["No items found"])
				else:
					window["lookup_list"].update(self.lookup_items)

		# Lookup List Event
		elif event == "lookup_list" and values["lookup_list"][0] not in ["Search key too short", "No items found", "Enter a search key above"]:
			index = window.Element('lookup_list').Widget.curselection()[0]
			RSGE_f.selected_item = RSGE_item.RSGE_item(self.lookup_ids[index])
			window["lookup_stats"].update(RSGE_f.selected_item)
			window["lookup_total"].update(f"{RSGE_f.generate_price(RSGE_f.selected_item.price, window['lookup_quantity'].get())} gp")
			window["lookup_image"].update(RSGE_f.selected_item.image)

		# Lookup Quantity Event
		elif event == "lookup_quantity" and RSGE_f.selected_item is not None:
			window["lookup_total"].update(f"{RSGE_f.generate_price(RSGE_f.selected_item.price, window['lookup_quantity'].get())} gp")

	# Creates lookup frame containing input box, search button, and results listbox elements
	def create_lookup_frame(self, lookup_item_frame):
		return sg.Frame(layout = 
							[
								[
									sg.Input(size = (25, 1), key = "lookup_input"), 
									sg.Button(button_text = "Search")
								],
								[
									sg.Listbox(values = ["Enter a search key above"], select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, size = (31, 10), enable_events = True, key = "lookup_list")
								],
								[
									lookup_item_frame
								]
							], 
							title = "Item Lookup")

	# Creates lookup frame containing selected lookup item's stats and image, with an add button and input box for quantity
	def create_lookup_item_frame(self):
		return sg.Frame(layout = 
									[
										[
											sg.Image(filename = "data/blank.png", size = (96,96), key = "lookup_image"),
											sg.Text(text = 
															"Name: N/A\n" +
															"Price: 0 gp\n" +
															"HA: 0 gp\n" +
															"Trend:\n" +
															" • 30 days: +0.0%\n" +
															" • 90 days: +0.0%\n" +
															" • 180 days: +0.0%", 
												key = "lookup_stats")
										],
										[
											sg.Button(button_text = "Add"), 
											sg.Input(default_text = "1", size = (10, 1), enable_events = True, key = "lookup_quantity"),
											sg.Text(text = "Total cost: 0 gp", key = "lookup_total")
										]
									], 
									title = "Item Stats")