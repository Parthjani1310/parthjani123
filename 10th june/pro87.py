# Find all duplicate characters in string....


string = input ("Enter string : ")
print("Duplicate characters is : ")

for i in range(0,len(string)):
    count = 1;

    for j in range(i+1,len(string)):
        if (string[i]==string[j]and string[i]!=''):
            count = count+1;

            string = string[:j]+"0"+string[j+1:];

    if (count>1 and string[i]!='0'):
        print(string[i]);

