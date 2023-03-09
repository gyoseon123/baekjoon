import heapq
import sys
input = sys.stdin.readline
n = int(input())
max_heap = []
min_heap = []
for _ in range(n):
    num = int(input())
    if len(max_heap) <= len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        temp = -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, temp)
    print(-max_heap[0])
