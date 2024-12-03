import sys
input = sys.stdin.readline

n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort()

ans = 0

idx = l[0][0]
now = l[0][1]

for i,h in l:
    if h >= now:
        ans += (i - idx)*now
        now = h
        idx = i

# print(ans)
# print(now, idx)

bidx = l[-1][0]
bnow = l[-1][1]

# print(bnow)

for i,h in l[::-1][1:]:
    if h > bnow:
        ans += (bidx - i)*bnow
        bnow = h
        bidx = i
    if i == idx: break

ans += now
# ans += now + (l[-1][0] - idx)*l[-1][1]

print(ans)