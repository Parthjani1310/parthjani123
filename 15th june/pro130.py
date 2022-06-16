# python - Linear search..

pos = -1

def  search(list,n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1

    return False

list = [15,55,19,40,1,78,99,43,78,32,35]
n = 99

if search(list,n):
    print("Found it ",pos)
else:
    print("Not Found")
