# find uncommon words from two Strings.....

def uncommon_words(s1, s2):
    count = {}
    for word in s1.split():
        count[word] = count.get(word, 0) + 1
    # words of string s2
    for word in s2.split():
        count[word] = count.get(word, 0) + 1
    # return required list of words
    return [word for word in count if count[word] == 1]

s1= input("Enter first string: ")
s2= input("Enter second string: ")
  
print(uncommon_words(s1, s2))