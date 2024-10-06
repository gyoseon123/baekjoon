import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    target = n*(n+1)//2
    
    left = 0
    right = int(1e9)+1
    
    while left + 1 < right:
        mid = (left+right)//2
        
        if mid*(mid+1) <= target:
            left = mid
        else:
            right = mid
    
    print(left+1)
    