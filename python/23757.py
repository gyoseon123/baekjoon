import sys
input = sys.stdin.readline
n,m = map(int, input().split())
gift = list(map(int, input().split()))
children = list(map(int, input().split()))
gift.sort()
children.sort()
now = 0
flag = False
for i in children:
    try:
        while i > gift[now]:
            now += 1
    except:
        flag = True
        break
    gift[now] -= i
print(gift)
if flag or gift[-1] < 0:
    print(0)
else:
    print(1)