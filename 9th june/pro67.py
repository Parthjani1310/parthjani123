# print even length words in a string...

def PrintEvenWords(s):

    s = s.split(' ')

    for word in s:
        if len(word) % 2 == 0:

            print(word)

string = input("Enter string: ")
PrintEvenWords(string)