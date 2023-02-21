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
lis.append(arr[0])
for i in arr[1:]:
    if i > lis[-1]:
        lis.append(i)
    else:
        pos = bin_search(i)
        lis[pos] = i
print(len(lis))