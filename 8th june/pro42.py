# Remove empty list from list...

list = [5, 6, '   ', 3,'', [], 9]
 
print("The list is : " + str(list))
 
res = [ele for ele in list if ele != []]
 
print("List after empty list removed : " + str(res))