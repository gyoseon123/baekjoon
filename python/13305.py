import sys
input = sys.stdin.readline
n = int(input())
road_len = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
sig = False
i = 0
while i < n:
    now = cost[i]
    for j in range(i+1,n):
        if cost[j] < now:
            result += now*sum(road_len[i:j])
            i = j
            break
        elif j == n-1:
            result += now*sum(road_len[i:n-1])
            i = n-1
    if i == n-1:
        break

print(result)
