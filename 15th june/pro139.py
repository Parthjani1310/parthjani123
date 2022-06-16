# Python Program for Heap Sort...

from heapq import heappop, heappush  
   
def heapsort(list):  
     heap = []  
     for ele in list:  
         heappush(heap, ele)  
   
     sort = []  
   
     
     while heap:  
         sort.append(heappop(heap))  
   
     return sort  
   
list = [27, 21, 55, 15, 60, 4, 11, 17, 2, 87]  
print(heapsort(list))  