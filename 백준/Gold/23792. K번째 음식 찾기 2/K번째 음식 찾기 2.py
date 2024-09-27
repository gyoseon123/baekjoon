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
    
    left = -1
    right = cq
    while left + 1 < right:
        mid = (left + right)//2
        if c[mid] > target:
            right = mid
        else:
            left = mid
    cc = right
    
    return (ac, bc, cc)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    aq, bq, cq, k = map(int, input().split())
    left = 0
    right = int(1e10)
    while left + 1 < right:
        mid = (left + right)//2
        ac, bc, cc = cnt(mid)
        abc = ac + bc + cc
        if abc > k:
            right = mid
        elif abc == k:
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
    
    if cc-1 >= 0 and c[cc-1] > ans:
        ans = c[cc-1]
        res = [3, cc]
        
    print(*res)