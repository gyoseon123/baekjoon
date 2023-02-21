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
l = []
for _ in range(n):
    a,b = map(int, input().split())
    l.append((a,b))
l.sort()
arr = [i[1] for i in l]
record = []
lis = []
lis.append(arr[0])
record.append(1)
for i in arr[1:]:
    if lis[-1] < i:
        lis.append(i)
        record.append(len(lis))
    else:
        pos = bin_search(i)
        lis[pos] = i
        record.append(pos+1)
target = len(lis)
result = []
for i in range(n-1, -1,-1):
    if record[i] != target:
        result.append(l[i][0])
    else:
        target -= 1
print(n-len(lis))        
print(*result[::-1], sep='\n')
