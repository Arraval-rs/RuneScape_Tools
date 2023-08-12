#####################################################
# RSGE_item.py                                      #
# Item objects used to hold various data            #
#####################################################

import RSGE_functions as RSGE_f

class RSGE_item:
	# default constructor
	def __init__(self, itemId, orig=None):
		if orig == None:
			url = 'https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}'.format(itemId)
			item_dict = RSGE_f.jsonDict(url, True)
			self.id = itemId
			self.name = item_dict['item']['name']
			self.quantity = 1
			self.description = item_dict['item']['description']
			self.price = RSGE_f.gazbot_dict[str(self.id)]["price"]
			self.highAlch = RSGE_f.gazbot_dict[str(self.id)]["highalch"] # TODO: handle no highalch attribute
			self.day30 = item_dict['item']['day30']['change']
			self.day90 = item_dict['item']['day90']['change']
			self.day180 = item_dict['item']['day180']['change']
			self.image = RSGE_f.imageUrl(item_dict['item']['icon_large'])
		else:
			self.id = orig.id
			self.name = orig.name
			self.quantity = orig.quantity
			self.description = orig.description
			self.price = orig.price
			self.highAlch = orig.highAlch
			self.day30 = orig.day30
			self.day90 = orig.day90
			self.day180 = orig.day180
			self.image = orig.image

	def __str__(self):
		return  (
					f"Name: {self.name}\n"\
					f"Price: {self.price}\n"\
					f"HA: {self.highAlch} gp\n"\
					f"Trend:\n" +
					f" • 30 days: {self.day30}\n" +
					f" • 90 days: {self.day90}\n" +
					f" • 180 days: {self.day180}"
				)