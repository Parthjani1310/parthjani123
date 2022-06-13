my_dict ={"dhruv":100, "those":121, "Aadi":189}
print("The dictionary is :")
print(my_dict)

dict_key = list(my_dict.keys())
print("The keys in the dictionary are :")
print(dict_key)
dict_val = list(my_dict.values())
print("The values in the dictionary are :")
print(dict_val)

my_position = dict_val.index(100)
print("The value at position 100 is : ")
print(dict_key[my_position])

my_position = dict_val.index(189)
print("The value at position 189 is")
print(dict_key[my_position])