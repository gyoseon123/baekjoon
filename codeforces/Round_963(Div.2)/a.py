import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().rstrip()

    ans = 0
    for w in ('A', 'B', 'C', 'D'):
        ans += min(n, s.count(w))
    print(ans)