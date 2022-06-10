# Find words which are greater than given length k...


def string_k(k, str):

    string = []

    text = str.split(" ")

    for x in text:

        if len(x) > k:

            string.append(x)

    return string


str = input("Enter string: ")
k = input("Enter value: ")
print(string_k(k, str))
