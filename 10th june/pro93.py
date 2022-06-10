# Merging two Dictionaries...

dict_1 = {1: 'TY', 2: 'Devops'}
dict_2 = {2: 'Javascript', 4: 'Python'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)