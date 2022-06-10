# Insertion at the beginning in OrderedDict...

from collections import OrderedDict

dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])

insrt = OrderedDict([("D", '400')])
  
final = OrderedDict(list(insrt.items())+list(dic1.items()))

print("The final Dictionary is : ")

print(final)