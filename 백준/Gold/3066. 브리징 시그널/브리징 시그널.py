import sys
input = sys.stdin.readline

def bs(target):
    left = -1
    right = len(lis)
    while left + 1 < right:
        mid = (left+right)//2
        if lis[mid] < target:
            left = mid
        else:
            right = mid
    return right

t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(input()) for _ in range(n)]
    lis = []
    lis.append(l[0])
    
    for num in l[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            pos = bs(num)
            lis[pos] = num
    print(len(lis))