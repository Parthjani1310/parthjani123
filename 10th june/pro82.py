#  Permutation of a given string using inbuilt function....

from itertools import permutations

def allPermutations(s):

    permList = permutations(s)

    for perm in list(permList):
        print(''.join(perm))

s = input("Enter string : ")
allPermutations(s)