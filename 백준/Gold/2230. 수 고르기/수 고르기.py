import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split())
if n == 1:
    print(0)
    exit()
    
l = [int(input()) for _ in range(n)]
l.sort()

left = 0
right = 0
ans = INF
now = 0

while True:
    if now <= m:
        right += 1
    else:
        left += 1
        
    if right >= n:
        break
    now = l[right] - l[left]
    if now >= m:
        ans = min(ans, now)

print(ans)
        
    
    