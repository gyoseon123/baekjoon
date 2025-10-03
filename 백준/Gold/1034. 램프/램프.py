from collections import defaultdict
import sys
input = sys.stdin.readline



n,m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
k = int(input())

d = defaultdict(int)

for line in board:
    d[line] += 1

ans = 0
for line in board:
    cnt = line.count('0')
    if (cnt <= k and (k - cnt)%2 == 0):
        ans = max(ans, d[line])

print(ans)