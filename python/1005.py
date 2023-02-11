from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    order = [[] for _ in range(n+1)]
    in_degree = [0]*(n+1)
    total_cost = cost[:]
    q = deque()
    for i in range(k):
        x,y = map(int, input().split())
        order[x].append(y)
        in_degree[y] += 1
    for i in range(1,n+1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in order[now]:
            total_cost[i] = max(total_cost[i], total_cost[now]+cost[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    w = int(input())
    print(total_cost[w])
    




t = int(input())
for i in range(t):
    solve()