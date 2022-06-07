# Find reminder of array multiplication divided by n

def reminder(arr,lens,n):
    mul = 1
    for i in arr:
        mul = mul * (i%n)
    return mul%n

arr = [200,35,14,36,40]
len = len(arr)
n = 11
print(reminder(arr,len,n))
