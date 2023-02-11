import sys
input = sys.stdin.readline
n,c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()
def check(s):
    cnt = 0
    now = house[0]
    for i in house[1:]:
        if i-now >= s:
            cnt += 1
            now = i
    if cnt+1 >= c:
        return True
    else:
        return False

left = 0
right = int(1e9)
while left <= right:
    min = (left+right)//2
    is_able = check(min)
    if is_able:
        left = min+1
    else:
        right = min-1
print((left+right)//2)