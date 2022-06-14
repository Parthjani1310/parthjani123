# Join Tuples if similar initial element...

from collections import defaultdict

List = [(11,12),(12,13),(12,14),(12,15),(16,17)]

print("The original list is : "+ str(List))

ddl = defaultdict(list) 
for key, val in List:
    ddl[key].append(val)

    result = [(key,*val) for key, val in ddl.items()]

print ("The list after joining : "+str(result))

