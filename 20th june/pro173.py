# Python Regex | Program to accept string ending with alphanumeric character...

import re

regex_expression = '[a-zA-z0-9]$'

def check_string(my_string):

   if(re.search(regex_expression, my_string)):
      print("The string ends with alphanumeric character")

   else:
      print("The string doesnot end with alphanumeric character")


string1 = "Parth@"
print("The string is :")
print(string1)
check_string(string1)

string2 = "Parth1310"
print("\nThe string is :")
print(string2)
check_string(string2)