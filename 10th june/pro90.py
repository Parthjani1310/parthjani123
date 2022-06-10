# to find the sum of all items in a dictionary...

def returnsum(dict):

    list = []
    for i in dict:
        list.append(dict[i])
    final = sum(list)

    return final

dict = input("Enter dictionary : ")
print("sum :",returnsum(dict) )