# Python – Remove Tuples of Length K...

list = [(5,6,7),(7,8),(9,10),(12,13)]

print("The  original list is : "+str(list))

k=2

result = [a for a in list if len(a)!=k]

print("The final list : "+str(result))