import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


t = int(input())
for i in range(t):
    max_heap = []
    min_heap = []
    valid = defaultdict(int)
    k = int(input())
    count_heappush = 0
    count_heappop = 0
    for i in range(k):
        x,n = input().split()
        if x == 'I':
            count_heappush += 1
            valid[int(n)] += 1
            heapq.heappush(max_heap,-int(n))
            heapq.heappush(min_heap,int(n))
        if x == 'D':
            if n == '-1':
                if min_heap:
                    count_heappop += 1
                    min_pop = heapq.heappop(min_heap)
                    while valid[min_pop] == 0:
                        if min_heap:
                            min_pop = heapq.heappop(min_heap)
                        else:
                            break
                    if valid[min_pop]:
                        valid[min_pop] -= 1
            if n == '1':
                if max_heap:
                    count_heappop += 1
                    max_pop = -heapq.heappop(max_heap)
                    while valid[max_pop] == 0:
                        if max_heap:
                            max_pop = -heapq.heappop(max_heap)
                        else:
                            break
                    if valid[max_pop]:
                        valid[max_pop] -= 1
                

    while max_heap:
        if valid[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        else:
            break
    while min_heap:
        if valid[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        else:
            break
        # while True:
        #     a,b = valid[-max_heap[0]], valid[min_heap[0]]
        #     if a != 0 and b != 0:
        #         break
        #     if a == 0:
        #         heapq.heappop(max_heap)
        #     if b == 0:
        #         heapq.heappop(min_heap)
    if max_heap and min_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')