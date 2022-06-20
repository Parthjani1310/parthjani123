# import module for regular expression

import re

def match(str,pattern):
  if re.search(pattern,str):
    print("valid string")
  else:
    print("invalid string")

pattern = re.compile('[A-Z]+$')
match('ABCDE',pattern)
match('12ABCda',pattern)
match('12345',pattern)