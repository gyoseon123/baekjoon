import sys
input = sys.stdin.readline
n,x = map(int, input().split())
cost = []
ans = 0
for _ in range(n):
    a,b = map(int, input().split())
    ans += b
    cost.append(a-b)
x -= n*1000
cost.sort(reverse=True)
for i in range(n):
    if x >= 4000 and cost[i] > 0:
        ans += cost[i]
        x -= 4000
    else:
        break
print(ans)
