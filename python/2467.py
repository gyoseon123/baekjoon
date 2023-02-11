import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
left = 0
right = n-1
result = int(1e9)*2
while left < right:
    now = l[left] + l[right]
    if abs(now) < result:
        result = abs(now)
        ansl = l[left]
        ansr = l[right]
    if now < 0:
        left += 1
    else:
        right -= 1

print(ansl, ansr)