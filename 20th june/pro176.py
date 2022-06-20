# Python Program to Check if an URL is valid or not using Regular Expression...

import re

def Find(string):

	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)	
	return [x[0] for x in url]

string = 'https://www.youtube.com/channel/UCpsBwReBY82nWUlMXP4jbOg'
print("Urls: ", Find(string))
	

