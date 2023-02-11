import heapq         
n,m = map(int, input().split())
icecream = list(map(int, input().split()))
is_reverse = False
q1 = []
q2 = []
visited = set()
for i in range(n):
    heapq.heappush(q1, (-icecream[i], i+1))
    heapq.heappush(q2, (-icecream[i], -(i+1)))

cnt = 0
while q1 and q2 and cnt < m:
    if not is_reverse:
        val, index = heapq.heappop(q1)
        val = -val
        if index not in visited:
            visited.add(index)
            if val%7 == 0:
                is_reverse = True
            print(index)
            cnt += 1
    else:
        val, index = heapq.heappop(q2)
        val = -val
        index = -index
        if index not in visited:
            visited.add(index)
            if val%7 == 0:
                is_reverse = False
            print(index)
            cnt += 1



