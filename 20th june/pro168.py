# Python Program to put spaces between words starting with capital letters using Regex...

import re

string = 'PjParthOp'
 
words = re.findall('[A-Z][a-z]*', string)

print(' '.join((words)))
