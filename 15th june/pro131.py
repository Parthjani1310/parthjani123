# Python Program for Insertion Sort...

list = int(input("Enter list : "))
a = []
 
for i in range (list):
    val = int(input("Enter number : "))
    a.append(val)


for j in range (1,list):
    t = a[i]
    i = i-1

    while j >= 0 and t<a[j]:
        a[j+1] = a[j]
        j=j-1

    a[j+1] = t

print("Sorted array : ")
print(a)