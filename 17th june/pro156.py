#Inverted Star Pyramid Pattern

rows = int(input('Enter the number of rows: '))

for a in range(rows,0,-1):
    for b in range(rows-a):
        print(' ', end='') 
    
    for b in range(2*a-1):
        print('*',end='') 
    print()