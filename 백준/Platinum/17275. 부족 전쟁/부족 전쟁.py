import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    
    indegree = [0]*(n+1)
    for _ in range(m):
        u,v = map(int, input().split())
        indegree[u] += 1
        indegree[v] += 1
    
    ans = n * (n-1) * (n-2) // 6
    cnt = 0
    for i in range(1, n+1):
        cnt += indegree[i] * (n - indegree[i] - 1)
    
    cnt //= 2
    print(ans - cnt)