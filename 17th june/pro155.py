# Python Program to print an Inverted Star Pattern...

rows = int(input("Enter the number of rows: "))  
 
for a in range(rows + 1, 0, -1):    
    for b in range(0, a - 1):  
        print("*", end=' ')  
    print(" ")