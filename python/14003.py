import sys
input = sys.stdin.readline

def bin_search(target):
    left = 0
    right = len(lis)-1
    while left < right:
        mid = (left+right)//2
        if lis[mid] < target:
            left = mid+1
        else:
            right = mid
    return right

n = int(input())
arr = list(map(int, input().split()))
lis = []
record = []
lis.append(arr[0])
record.append(1)
for i in arr[1:]:
    if i > lis[-1]:
        lis.append(i)
        record.append(len(lis))
    else:
        pos = bin_search(i)
        lis[pos] = i
        record.append(pos+1)
print(len(lis))
target = len(lis)
result = []
for i in range(n-1,-1,-1):
    if record[i] == target:
        result.append(arr[i])
        target -= 1
print(*result[::-1])