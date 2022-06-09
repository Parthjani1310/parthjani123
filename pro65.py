# Convert Snake case to Pascal case....

from string import capwords

string = input("Plese enter string:")
print ("The snake case is: ",string)

pascal = capwords(string.replace('_',''))
pascal = pascal.replace(' ','')

print("The snake case is: ",pascal)

