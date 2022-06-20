# Python Regex to extract maximum numeric value from a string...

import re

string = '12abcop500pj1310'

number = re.findall('\d+', string)

number = map(int, number)

print("Max_value:",max(number))