import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
l.sort()
left = 0
right = n-1


result = ()
while left < right-1:
    mix = l[left] + l[right]
    if mix < 0:
        left += 1
    else:
        right -= 1

print(left,right)