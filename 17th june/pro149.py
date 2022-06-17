# Python Program for Gnome Sort....

def gnome_sort(array):
    for position in range(1, len(array)):
        while (position != 0 and array[position] < array[position - 1]):
            array[position], array[position - 1] = array[position - 1], array[position]
            position = position - 1 
 
 
array = input('Enter the numbers: ').split()
array = [int(a) for a in array]
gnome_sort(array)
print('The sorted array is: ', end='')
print(array)