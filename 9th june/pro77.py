#  split and join a string....

def split_string(string):
    
    list_string = string.split(' ')
    
    return list_string

def join_string(list_string):
    
    string = '-'.join(list_string)
    
    return string

string = input("Enter string: ")

list_string = split_string(string)

print("After Splitting: ",list_string)

res_string = join_string(list_string)

print("After joining: ",res_string)