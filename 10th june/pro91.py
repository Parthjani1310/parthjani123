# Ways to remove a key from dictionary....

dict = {"vidyut" : "martial",
        "dhoni" : "cricketer",
        "marks" : "5,6,9,"}

print("The actual dictionary is : "+str(dict))

del dict["dhoni"]

print("First removed dictionary is : "+str(dict))

del dict["marks"]

print("Second removed dictionary is : "+str(dict))