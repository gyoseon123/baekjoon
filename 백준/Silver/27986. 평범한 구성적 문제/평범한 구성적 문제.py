import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]

minitv = INF

for lo, hi in l:
    minitv = min(minitv, hi - lo + 1)

arr = [i for i in range(1, minitv+1)]
target = 0

for i in range(n):
    print(arr[target], end=' ')
    target += 1
    target %= minitv