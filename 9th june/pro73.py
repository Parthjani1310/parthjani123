# Program to check if a string contains any special character...

import re

def find(string):
    special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    
    if special_char.search(string) == None:
        return "string is accepted"
    else:
        return "string not accpeted"
   

s= input("Plese enter string: ")
print(s)
print(find(s))