import sys
iuput = sys.stdin.readline

n,k = map(int, input().split())

up = []
down = []

for _ in range(n):
    x,m = map(int, input().split())
    if x > 0:
        up.append([x,m])
    else:
        down.append([x,m])

up.sort()
down.sort(reverse=True)

ans = 0
while down:
    now = k*((down[-1][1]-1)//k+1)
    ans += -down[-1][0]*2*((down[-1][1]-1)//k+1)
    while down[-1][1] <= now:
        now -= down[-1][1]
        down.pop()
        if not down:
            break
    if down:
        down[-1][1] -= now

while up:
    now = k*((up[-1][1]-1)//k+1)
    ans += up[-1][0]*2*(((up[-1][1]-1)//k+1))
    while up[-1][1] <= now:
        now -= up[-1][1]
        up.pop()
        if not up:
            break
    if up:
        up[-1][1] -= now

print(ans)

