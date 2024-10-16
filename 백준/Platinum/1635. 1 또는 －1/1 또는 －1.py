import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []

for i in range(n):
    arr.append([-1]*i + [1]*(n-i))

for _ in range(m):
    q = list(map(int, input().split()))
    for i in range(n):
        ret = 0
        for j in range(n):
            ret += q[j]*arr[i][j]
        if ret == 0:
            print(*arr[i])
            break
    