# to sort list of dictionaries by values in Python – Using itemgetter..

from operator import itemgetter

list = [{ "name" : "Ajay", "age" : 16},
          { "name" : "Rahul", "age" : 20 },
          { "name" : "Sahil" , "age" : 24 },
          { "name" : "Jinal" , "age" : 26 }] 

print("The  list sorted by age is : ")
print(sorted(list, key=itemgetter("age")))

print("The list sorted by age and name is : ")
print(sorted(list, key=itemgetter('age', 'name')))