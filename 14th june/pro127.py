# Python – Flatten tuple of List to tuple...

tuple = ([9, 1], [5, 7, 2, 3], [7])
  

print("The original tuple : " + str(tuple))
  

res = tuple(sum(tuple, []))
  

print("The flattened tuple : " + str(res))