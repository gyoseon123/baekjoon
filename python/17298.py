import sys
from collections import deque
input = sys.stdin.readline
a = int(input())
table = list(map(int, input().split()))
q = []
result = [0] * a
target = 1
for i in range(a):
    q.append(i)
    if table[q[-1]] < table[target]:
        while q:
            x = q.pop()
            result[x] = table[target]
            target += 1
    else:
        target += 1
print(result)
