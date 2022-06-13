# Possible Words using given characters in Python...

def charcount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i,0)+1
        return dict

def possible_words(lword,charset):
    for  word in lword:
        flag = 1
        chars = charcount(word)
        for key in chars:
            if key not in  charset:
                flag = 0
            else:
                if charset.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)

if __name__ == "__main__":
    input = ['roo', 'bowl', 'you', 'eat', 'roll', 'girl', 'can']
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    possible_words(input, charSet)
