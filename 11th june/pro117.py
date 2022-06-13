# Python – Maximum and Minimum K elements in Tuple...

def Findel(tup,K):
    
    tup = list(tup)
    
    temp = sorted(tup)
    
    result = tuple(temp[:K] + temp[-K:])
  
    print("Max and Min K elements : ",result)

tup = (13, 10, 23, 2, 5, 6, 12, 7, 1, 8)

K = 2

print("The original tuple: ", tup)

Findel(tup,K)
