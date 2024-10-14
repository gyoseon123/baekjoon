import heapq

p1, p2, p3, i = map(int, input().split())

arr = []
q = []
heapq.heappush(q, p1)
heapq.heappush(q, p2)
heapq.heappush(q, p3)

used = set([p1, p2, p3])
target = 0

while True:
    now = heapq.heappop(q)
    arr.append(now)
    if now*p1 <= int(1e18) and now*p1 not in used:
        heapq.heappush(q, now*p1)
        used.add(now*p1)
    if now*p2 <= int(1e18) and now*p2 not in used:
        heapq.heappush(q, now*p2)
        used.add(now*p2)
    if now*p3 <= int(1e18) and now*p3 not in used:
        heapq.heappush(q, now*p3)
        used.add(now*p3)
    target += 1
    if min(now*p1, now*p2, now*p3) > int(1e18): break

while q:
    arr.append(heapq.heappop(q))

print(sorted(list(set(arr)))[i-1])