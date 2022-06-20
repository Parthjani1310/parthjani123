# Python | Remove all characters except letters and numbers...

import re

my_string = "parth1310:, @.com"

print ("The string is : ")

print(my_string)

result = re.sub('[\W_]+', '', my_string)

print ("The expected string is :")

print(result)