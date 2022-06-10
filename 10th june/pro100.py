# Sort Dictionary key and values List...

my_dict = {'Dhruv': [1, 6, 3],
   'bhargav': [2, 9, 6],
   'parth': [16, 7]}

print("The dictionary is : ")
print(my_dict)

my_result = dict()
for key in sorted(my_dict):
   my_result[key] = sorted(my_dict[key])

print("The sorted dictionary is : " )
print(my_result)-