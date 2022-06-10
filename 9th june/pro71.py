# Least Frequent Character in String...

string= input("Enter String: ")

print(string)

char_freq={}

for i in string:

    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i] = 1

result= min(char_freq, key = char_freq.get)

print("Least frequent character: ",result)