# Python Program to Remove duplicate words from Sentence...

s = "Virat kohali is one of the best batter in cricket world virat"
l = s.split()
k = []
for i in l:
 
    # If condition is used to store unique string
    # in another list 'k'
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))