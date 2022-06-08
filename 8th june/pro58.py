# Vertical concatenate...

from numpy import array, concatenate



A = array([1,2,3,4])
B = array([5,6,7,8])

C  = concatenate((A,B),axis=0)

print("Concetination is: ",C)