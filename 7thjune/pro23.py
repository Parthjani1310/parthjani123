def InterchangeList(list):
       
    first = list.pop(0)   
    last = list.pop(-1) 
    list.insert(0, last)  
    list.append(first)         
    return list

li = [1, 9, 2, 10, 19, 30]
print(li)
print("Interchange is: ",InterchangeList(li))