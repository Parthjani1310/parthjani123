# Python – All pair combinations of 2 tuples...

from itertools import product,chain


tuple1 = (1,2)
tuple2 = (3,4)

print("The tuple1 : "+str(tuple1))
print("The tuple2 : "+str(tuple2))

result = list(chain(product(tuple1,tuple2), product(tuple2,tuple1)))

print("The final tuple is : "+str(result))
