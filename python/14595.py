import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
if m == 0:
    print(n)
    exit()
action = []
for i in range(m):
    action.append(tuple(map(int, input().split())))
action.sort()

tx,ty = action[0]
cnt = 0
cnt += tx-1
for x,y in action[1:]:
    if x <= ty:
        ty = max(y, ty)
    else:
        cnt += x-ty
        tx,ty = x,y
cnt += n-ty+1
print(cnt)

