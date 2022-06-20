# Python Regex – Program to accept string starting with vowel...

string = input('Enter the String: ')

vowel = 'aeiou'

if string[0].lower() in vowel:
   print(string,'starts with vowel',string[0])
else:
   print(string,'starts with consonant',string[0])