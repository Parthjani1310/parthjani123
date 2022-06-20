# Python – Check whether a string starts and ends with the same character or not...


import re

string = 'rj1310jr'

expression = r'^[a-z]$|^([a-z]).*\1$'

if(re.search(expression,string)):

  print("Valid input")

else:

  print("Invalid input")
