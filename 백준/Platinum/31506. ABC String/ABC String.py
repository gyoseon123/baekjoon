import sys
input = sys.stdin.readline

s = input().rstrip()
cnt = [0]*3

ans = 0
for w in s:
    if w == "A": cnt[0] += 1
    elif w == "B": cnt[1] += 1
    else: cnt[2] += 1
    mn = min(cnt)
    for i in range(3): cnt[i] -= mn
    ans = max(ans, max(cnt))

print(ans)