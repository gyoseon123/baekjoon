import sys
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split()))
ans = sum(w)
for _ in range(n-1):
    a,b = map(int, input().split())
    ans -= min(w[a], w[b])
print(ans)