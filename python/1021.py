from collections import deque
a,b = map(int, input().split())
l = deque(list(map(int, input().split())))
num = deque([i for i in range(1,a+1)])
cnt = 0
while len(l) != 0:
    if num[0] == l[0]:
        l.popleft()
        num.popleft()
    else:
        if num.index(l[0]) <= len(num)//2:
            num.rotate(-1)
            cnt += 1
        else:
            num.rotate(1)
            cnt += 1
print(cnt)
