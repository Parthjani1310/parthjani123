# Python Program for Iterative Merge Sort...

def merge(S, temp, From, mid, to):
 
    a = From
    b = From
    c = mid + 1
 
    while b <= mid and c <= to:
        if S[b] < S[c]:
            temp[a] = S[b]
            b = b + 1
        else:
            temp[a] = S[c]
            c = c + 1
        a = a + 1
 
    while b < len(S) and b <= mid:
        temp[a] = S[b]
        a = a + 1
        b = b + 1
 
    for b in range(From, to + 1):
        S[b] = temp[b]
 
def Merge_Sort(S):
 
    low = 0
    high = len(S) - 1
 
    temp = S.copy()
 
    d = 1
    while d <= high - low:
 
        for b in range(low, high, 2*d):
            From = b
            mid = b + d - 1
            to = min(b + 2*d - 1, high)
            merge(S, temp, From, mid, to)
 
        d = 2*d
 
if __name__ == '__main__':
 
    S = [4, 2, 3, 1, 6, 5]
    print("The Original array is: ", S)
    Merge_Sort(S)
    print("Array after sorting is: ", S)