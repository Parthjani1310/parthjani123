# Python Program for Odd-Even Sort / Brick Sort...

def oddEvenSort(arr, n):
    # flag
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
    return


arr = [1, 4, 2, 3, 6, 5, 8, 7]
n = len(arr)
oddEvenSort(arr, n)
print("Sorted sequence is : ")
for i in range(0, n):
    print(arr[i], end=" ")
