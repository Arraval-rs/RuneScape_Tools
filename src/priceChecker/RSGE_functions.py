#####################################################
# RSGE_functions.py                                 #
# Various functions and variables used by the		#
# Price Checker	tool								#
#####################################################
import os
import io
import json
import urllib.request
from datetime import datetime
from datetime import timedelta

import generalFunctions as func


# Poll the RS GE API for the last updated date
# Somewhat irrelevant as gazbot prices are updated daily
def lastUpdate():
	url = 'https://secure.runescape.com/m=itemdb_rs/api/info.json'
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	date = datetime.fromisoformat('2002-02-27') + timedelta(days=data['lastConfigUpdateRuneday'])
	sinceUpdate = datetime.now() - date
	return 'Last Updated {} ({} ago)'.format(date, sinceUpdate)

# retreives image data from a given url
def imageUrl(url):
	request = urllib.request.Request(url, headers = {"User-Agent" : "Magic Browser"})
	content = urllib.request.urlopen(request)
	return content.read()

# Generates an abbreviated price for input price and quantity i.e. 10k for 10000
def generate_price(price, quantity):
	try:
		if not quantity.isnumeric():
			quantity = 0
	except AttributeError:
		return price*quantity
	return price*int(quantity)

# List of tracked items
tracked_items = []

# Item selected in lookup frame
selected_item = None