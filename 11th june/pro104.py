# K’th Non-repeating Character in Python using List Comprehension and OrderedDict...

def first_non_repating_charcter(str1):

    char_order = []
    ctr = {}

    for c in str1:
        if c in ctr:
            ctr[c]+=1
        else:
         ctr[c]=1
         char_order.append(c)

    for c in char_order:
        if ctr[c]==1:
            return c
    return None

print(input("The first non-repeating character : ",))
print(input("The first non-repeating character : ",))
print(input("The first non-repeating character : ",))
