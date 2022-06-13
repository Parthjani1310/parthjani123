# Handling missing keys in Python dictionaries....

fruits_dict = {'Apple':'in','Mango':'in','Banana':'in'}

print(fruits_dict.get('Mango','Not found'))
print(fruits_dict.get('kiwi','Not found'))

