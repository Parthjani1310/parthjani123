#  Append Dictionary Keys and Values ( In order ) in dictionary...

dict = {"January" : 1, "Feb" : 2, "March" : 3, 
        'April':4, 'May' : 5, 'June' :6}

print("The dictionary is : ")
print(dict)

my_result = list(dict.keys()) + list(dict.values())

print("The ordered key and value are : ")
print(my_result)