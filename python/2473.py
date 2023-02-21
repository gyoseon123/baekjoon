import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
INF = int(1e9)*3
result = INF

for i in range(n):
    for j in range(i+1,n):
        left, right =  i,j
        l = 0
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if mid == left:
                l += 1
                continue
            if mid == right:
                r -= 1
                continue
            mixed = arr[left] + arr[mid] + arr[right]
            if abs(mixed) < result:
                result = abs(mixed)
                result_info = (left, mid, right)
            if mixed < 0:
                l = mid+1
            else:
                r = mid-1

print(*sorted([arr[i] for i in result_info]))