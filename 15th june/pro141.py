# Python Program for ShellSort...

def shell_sort(list, n):
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = [i]
            j = i
            while j >= h and list[j - h] > t:
                list[j] = list[j - h]
                j -= h
 
            list[j] = t
        h = h // 2
 
 
list= [34, 12, 20, 7, 13, 15, 2, 23]
n= len(list)
print('Array before Sorting:')
print(list)
shell_sort(list, n)
print('Array after Sorting:')
print(list)
