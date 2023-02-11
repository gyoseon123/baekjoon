import heapq
import sys
input = sys.stdin.readline
n = int(input())

def trans(t):
    time = t.split(':')
    result = []
    for s in time:
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1
        s = float(s[min(i, len(s)-1):])
        result.append(s)
    return result
    
def compare(x):
    return (x[0][0], x[0][1], x[0][2])

bus = []

ans = 0
for i in range(n):
    bus_in, bus_out = input().rstrip().split()
    bus.append((trans(bus_in), trans(bus_out)))
bus.sort(key=compare)
q = []
heapq.heappush(q, bus[0][1])
ans = len(q)
for x,y in bus[1:]:
    while q and q[0] <= x:
        heapq.heappop(q)
    heapq.heappush(q, y)
    ans = max(ans, len(q))

print(ans)