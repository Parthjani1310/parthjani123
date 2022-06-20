# Parsing and Processing URL using Python – Regex...

import re

s = 'https://www.youtube.com/channel/UCpsBwReBY82nWUlMXP4jbOg'


obj1 = re.findall('(\w+)://',
				s)
print("The protocol is : ",obj1)

obj2 = re.findall('://www.([\w\-\.]+)',
				s)
print("The site is : ",obj2)
