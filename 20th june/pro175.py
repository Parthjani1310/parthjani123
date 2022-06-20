# Python Program to check if a string starts with a substring using regex...

import re

def check_string(my_string, sub_string) :

   if (sub_string in my_string):

      concat_string = "^" + sub_string
      result = re.search(concat_string, my_string)

      if result :
         print("The string starts with the given substring")
      else :
         print("The string doesnot start with the given substring")

   else :
      print("It is not a substring")

string = input("Enter string : ")
sub_string = input("Enter sub-string : ")

print("The string is :")
print(string)

print("The sub-string is :")
print(sub_string)

check_string(string, sub_string)