# Check if binary representations of two numbers are anagram...

from collections import Counter


def checkAnagram(a,b):
    bin1 = bin(a)[2:]
    bin2 = bin(b)[2:]

    zeros = abs(len(bin1)-len(bin2))
    if (len(bin1)>len(bin2)):
        bin2 = zeros*'0'+bin2
    else:
        bin1 = zeros*'0'+bin1
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)

    if dict1 == dict2:
        print('yes')
    else:
        print('no')

a = input("Enter first number : ")
b = input("Enter second number : ")
checkAnagram(a,b)
