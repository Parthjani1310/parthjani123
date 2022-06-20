# Python Program to find the most occurring number in a string using Regex...

import re
import collections

string = 'AlwayS11avsilble123.1310'

number = re.findall(r"[0-9]", string)

counter = collections.Counter(number)

max_count = 0

max_value = None

for key in list(counter.keys()):

  if(counter[key]>max_count):
    max_count = counter[key]
    max_value = int(key)

print("max_value is : ",max_value)