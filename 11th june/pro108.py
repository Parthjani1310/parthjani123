# Python Dictionary to find mirror characters in a string...

from audioop import reverse
from sys import prefix


def mirrorchars(input,k):

    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'

    dictchars = dict(zip(original,reverse))

    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    for i in range(0,len(suffix)):
        mirror = mirror + dictchars[suffix[i]]

    print (prefix+mirror)

if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorchars(input,k)
