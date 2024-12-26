import sys
input = sys.stdin.readline

n = int(input())
mw = list(map(int, input().split()))
m = int(input())
w = list(map(int, input().split()))

mw.sort(reverse=True)
w.sort(reverse=True)
visit = [False]*m

target = 0
ans = 0
while True:
    ans += 1
    flg = False
    for i in range(m):
        if not visit[i] and mw[target] >= w[i]:
            flg = True
            visit[i] = True
            target += 1
            if target == n:
                break

    target = 0

    if not flg:
        break

print(ans-1 if visit.count(True) == m else -1)