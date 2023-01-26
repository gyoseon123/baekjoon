from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
table = [deque() for _ in range(21)]
ans = 0
for i in range(n):
    s = input().rstrip()
    while table[len(s)] and i-table[len(s)][0] > k: table[len(s)].popleft()
    ans += len(table[len(s)])
    table[len(s)].append(i)

print(ans)