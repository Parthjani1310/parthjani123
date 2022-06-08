from unicodedata import digit


# Sum of number digit in list...

list = [11, 23, 41, 62, 89, 0, 10]
print("The list is : ")
print(list)
my_result = []
for elem in list:
   sum_val = 0
   for digit in str(elem):
      sum_val += int(digit)
   my_result.append(sum_val)
print ("The result after adding the digits is : " )
print(my_result)