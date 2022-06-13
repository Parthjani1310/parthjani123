# Python counter and dictionary intersection example (Make a string using deletion and rearrangement)...

from collections import Counter


def make_string(str_1, str_2):
    dict_1 = Counter(str_1)
    dict_2 = Counter(str_2)

    result = dict_1 & dict_2
    return result == dict_1

string_1 = 'Hii there'
string_2 = 'how r u'
print("The first string is : ")
print(string_1)
print("The second string is : ")
print(string_2)

if (make_string(string_1, string_2)):
        print("It is possible")
else:
        print("It is not possible")

