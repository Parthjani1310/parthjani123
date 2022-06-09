# Ways to remove i’th character from string in Python...

a = "kdkgjsvnsd"

print ("The orignal strinng is : "+a)

A = " "
  
for i in range(len(a)):
    if i != 2:
        A = A + a[i]

print ("The string after removal : "+A)
