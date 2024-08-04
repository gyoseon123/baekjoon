t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    s = input()
    ans = 0
    p = "ABCDEFG"
    for w in p:
        ans += max(0, m - s.count(w))
    print(ans)