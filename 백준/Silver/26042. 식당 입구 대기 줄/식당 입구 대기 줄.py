import sys
input = sys.stdin.readline

n = int(input())
now = 0
max_p = -1
res = -1
for _ in range(n):
    q = list(map(int, input().split()))
    if len(q) == 1:
        now -= 1
    else:
        now += 1
        if now > max_p:
            max_p = now
            res = q[1]
        
        if now == max_p:
            res = min(res, q[1])

print(max_p, res)
