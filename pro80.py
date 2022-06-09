# Replace duplicate Occurrence in String....

str = input("Enter string: ")

print("The string is : ")

print(str)

replace_dict = {' ' : ' ' }

my_list = str.split(' ')

my_result = ' '.join([replace_dict.get(val) if val in replace_dict.keys() and my_list.index(val) != idx else val for idx, val in enumerate(my_list)])

print("The string after replacing with values is : ")

print(my_result)