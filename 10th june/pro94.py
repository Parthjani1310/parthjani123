# Convert key-values list to flat dictionary...

dic= { "day": [1, 2, 3], "name": ['Mon', 'Tues', 'Wed' ] }

print("Original dictionary: ",dic)

f_dic= dict(zip(dic["day"], dic["name"]))

print("FLATTENED DICTIONARY: ", f_dic)
