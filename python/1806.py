import sys
input = sys.stdin.readline
n,s = map(int, input().split())
num = [0] + list(map(int, input().split()))
for i in range(1,n):
    num[i+1] += num[i]
left = 0
right = 1
min_len = n+1
while left <= right and right <= n:
    csum = num[right] - num[left]
    if csum >= s:
        min_len = min(right-left, min_len)
        left += 1
    else:
        right += 1
if min_len == n+1:
    print(0)
else:
    print(min_len)