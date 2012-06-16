# File: heapq-example-1.py

import heapq

heap = []

# add some values to the heap
for value in [20, 10, 30, 50, 40]:
    heapq.heappush(heap, value)

# pop them off, in order
while heap:
    print heapq.heappop(heap),
