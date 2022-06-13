# Remove all duplicates words from a given sentence...

import string

string = 'virat is great and rohit is also great'

print (' '.join(dict.fromkeys(string.split())))
