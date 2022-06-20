# Python Program to Check if email address valid or not...

import re

def solve(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

s = "parthjani1310@gmail.com"
print(solve(s))