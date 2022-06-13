# Create a list of tuples from given list having number and its cube in each tuple...

def cubeoflist(li):

    result=[(num, num**2) for num in li]
    return result

li = [3, 4, 1, 2]

print(cubeoflist(li))