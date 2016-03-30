# _*_ coding:utf-8 _*_
# heappush 
from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print heap
heappush(heap, 0.5)
print heap
# heappop
print heappop(heap)
print heappop(heap)
print heappop(heap)
print heappop(heap)
print heap
# heapify
heap = [9 ,8 ,7 ,6 ,1 ,2 ,5 ,4]
heapify(heap)
print heap
# heapreplace
heapreplace(heap, 0.5)
print heap