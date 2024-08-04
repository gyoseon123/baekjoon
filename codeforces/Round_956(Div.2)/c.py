import sys
import math
input = sys.stdin.readline

def solve(a,c):
    left = 0
    sa = 0
    while sa < tot and left < n:
        sa += a[left]
        left += 1
    right = n-1
    sc = 0
    while sc < tot and right > 0:
        sc += c[right]
        right -= 1
    
    return (left, right)


t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    tot = math.ceil(sum(A)/3)

    l,r = solve(A,C)
    if l <= r and sum(B[l:r+1]) >= tot:
        print(1,l,l+1,r+1,r+2,n) #c
        continue

    l,r = solve(A,B)
    if l <= r and sum(C[l:r+1]) >= tot:
        print(1,l,r+2,n,l+1,r+1) #c
        continue

    l,r = solve(B,C)
    if l <= r and sum(A[l:r+1]) >= tot:
        print(l+1,r+1,1,l,r+2,n) #c
        continue

    l,r = solve(B,A)
    if l <= r and sum(C[l:r+1]) >= tot:
        print(r+2,n,1,l,l+1,r+1) #c
        continue

    l,r = solve(C,A)
    if l <= r and sum(B[l:r+1]) >= tot:
        print(r+2,n,l+1,r+1,1,l) #c
        continue

    l,r = solve(C,B)
    if l <= r and sum(A[l:r+1]) >= tot:
        print(l+1,r+1,r+2,n,1,l) #c
        continue

    print(-1)


