# Python program to Order Tuples using external List...

my_list = [("Aarya",35),("Jay",61),("sam",25)]
print("The list of tuple is : ")
print(my_list)

ordered_list = ['Jay', 'Aarya', 'sam']
print("The ordered list is :")
print(ordered_list)
temp = dict(my_list)

my_result = [(key, temp[key]) for key in ordered_list]

print("The ordered tuple list is : ")
print(my_result)