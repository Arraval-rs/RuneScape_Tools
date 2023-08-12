#####################################################
# RSGE_geSummary.py                                 #
# GE item summary elements and functions            #
#####################################################

import PySimpleGUI as sg
import RSGE_functions as RSGE_f
import RSGE_item

class GeWindow:
	def __init__(self):
		self.summary_frame = self.create_summary_frame(self.create_summary_item_frame())
		self.items = []

	def update_widgets(self, window, event, values):

		# Add Button Event
		# Need to check if already added
		if event == "Add" and RSGE_f.selected_item is not None and window["lookup_quantity"].get().isnumeric() and int(window["lookup_quantity"].get()) > 0:
			RSGE_f.selected_item.quantity = int(window["lookup_quantity"].get())
			self.items.append(RSGE_item.RSGE_item(None, RSGE_f.selected_item))
			item_strings = []
			total_cost = 0
			for item in self.items:
				item_strings.append(f"{item.quantity}x {item.name}")
				total_cost += item.price*item.quantity
				window["total_cost"].update(f"Total Cost: {RSGE_f.generate_price(total_cost, 1)} gp")
			window["summary_list"].update(item_strings)

		# Summary List Event
		if event == "summary_list" and values["summary_list"][0] != "Add an item to track":
			index = window.Element('summary_list').Widget.curselection()[0]
			window["summary_stats"].update(self.items[index])
			window["summary_total"].update(f"Quantity: {self.items[index].quantity}\nTotal Cost: {RSGE_f.generate_price(self.items[index].price, self.items[index].quantity)} gp")
			window["summary_image"].update(self.items[index].image)

		# Remove Button Event
		if event == "Remove" and len(self.items) > 0 and len(window["summary_list"].get()) > 0:
			print(window["summary_list"].get())
			print("Remove item pls")
			index = window.Element('summary_list').Widget.curselection()[0]
			self.items.remove(self.items[index])
			if len(self.items) == 0: 
				window["summary_list"].update(["Add an item to track"])
			else:
				window["summary_list"].update(self.items)
			return

	def create_summary_item_frame(self):
		return sg.Frame(layout = 
									[
										[
											sg.Image(filename = "data/blank.png", size = (96,96), key = "summary_image"),
											sg.Text(text = 
															"Name: N/A\n" +
															"Price: 0 gp\n" +
															"HA: 0 gp\n" + 
															"Trend:\n" +
															" • 30 days: +0.0%\n" +
															" • 90 days: +0.0%\n" +
															" • 180 days: +0.0%", 
												key = "summary_stats")
										],
										[
											sg.Button(button_text = "Remove"),
											sg.Text(text = "Quantity: 0\nTotal Cost: 0 gp", key = "summary_total")
										]
									],
									title = "Tracked Items")

	# Save Button
	# Load Button
	# Load Popup (different profiles)

	def create_summary_frame(self, summary_item_frame):
		return sg.Frame(layout = 
									[
										[
											sg.Text(text = "Total Cost: 0 gp", key = "total_cost")
										],
										[
											sg.Listbox(values = ["Add an item to track"], select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, size = (31, 10), enable_events = True, key = "summary_list")
										],
										[summary_item_frame],
									],
									title = "Tracked Items")