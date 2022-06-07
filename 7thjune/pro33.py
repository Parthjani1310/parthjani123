list1 = [10,40,40,60,75,89,89]
 
list2 = list(set(list1))

print(list2)
 
list2.sort()
 
print("Second largest element is: ", list2[-2])