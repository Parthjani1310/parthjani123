# Remove all duplicates from a given string in Python...

from collections import OrderedDict
from multiprocessing.reduction import duplicate
from os import remove
from re import S


def remove_duplicate(s):
    return "".join(OrderedDict.fromkeys(s))

    s= input("Enter string: ")
    print(s)
    print("After removing duplicates: ",remove_duplicate(S))
