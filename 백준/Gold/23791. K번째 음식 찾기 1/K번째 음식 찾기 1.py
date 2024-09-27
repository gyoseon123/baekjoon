import sys
input = sys.stdin.readline

def cnt(target):
    left = -1
    right = aq
    while left + 1 < right:
        mid = (left + right)//2
        if a[mid] > target:
            right = mid
        else:
            left = mid
    ac = right
    
    left = -1
    right = bq
    while left + 1 < right:
        mid = (left + right)//2
        if b[mid] > target:
            right = mid
        else:
            left = mid
    bc = right
    
    return (ac, bc)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    aq, bq, k = map(int, input().split())
    left = 0
    right = int(1e10)
    while left + 1 < right:
        mid = (left + right)//2
        ac, bc = cnt(mid)
        ab = ac + bc
        if ab > k:
            right = mid
        elif ab == k:
            break
        else:
            left = mid
    
    ans = -1
    if ac-1 >= 0 and a[ac-1] > ans:
        ans = a[ac-1]
        res = [1, ac]
    
    if bc-1 >= 0 and b[bc-1] > ans:
        ans = b[bc-1]
        res = [2, bc]

    print(*res)