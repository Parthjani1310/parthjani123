# Categorize Password as Strong or Weak using Regex in Python...

import re

v=input("Enter the password:")

if(len(v)>=8):

    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")

else:
    print("You have entered an invalid password.")