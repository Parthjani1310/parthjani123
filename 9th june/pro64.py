# Words Frequency in String Shorthands...

test_str = "Earth is round. "

print("The orignal string is:"+str(test_str))

res = {key: test_str.count(key)


for key in str.split()}

print ("The word frequency: "+str(res))

