# Sort a list of tuples by second Item...

tuple = [(500,4),(100,8),(300,2),(900,10)]
print("The orignal list is : ",tuple)
def sort(tuple):
    return(sorted(tuple, key = lambda a:a[1]))

print("sorted list is : ",sort(tuple))
