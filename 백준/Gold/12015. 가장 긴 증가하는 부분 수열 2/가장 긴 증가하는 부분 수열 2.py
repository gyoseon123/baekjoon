import bisect
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = []
lis.append(arr[0])
for i in arr[1:]:
    if i > lis[-1]:
        lis.append(i)
    else:
        pos = bisect.bisect_left(lis, i)
        lis[pos] = i
print(len(lis))
