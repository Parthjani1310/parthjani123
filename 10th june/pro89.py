# Extract Unique values dictionary values...

dict = {"vidyut" : "martial",
        "dhoni" : "cricketer",
        "marks" : "5,6,9,"}

print("The original dictionary is : ",dict)

res = list(sorted({ele for val in dict.values() 
        for ele in val}))

print ("The unique value list is : ",res)