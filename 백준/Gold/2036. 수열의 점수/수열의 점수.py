import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

up = []
down = []

for num in l:
    if num > 0:
        up.append(num)
    else:
        down.append(num)

up.sort(reverse=True)
down.sort()

ans = 0

if len(up)&1:
    ans += up[-1]
    
for i in range(0, len(up)-1, 2):
    fir = up[i]
    sec = up[i+1]
    if fir == 1 or sec == 1:
        ans += (fir + sec)
    else:
        ans += fir*sec

if len(down)&1:
    ans += down[-1]
    
for i in range(0, len(down)-1, 2):
    ans += down[i]*down[i+1]

print(ans)