import sys
input = sys.stdin.readline

def check(num):
    left = 0
    right = int(1e18)+1
    while left + 1 < right:
        mid = (left + right)//2
        if mid*mid >= num:
            right = mid
        else:
            left = mid
    
    return right*right == num

n = int(input())
l = list(map(int, input().split()))
ll = sorted(l[:])

flg = True
for i in range(n):
    x = l[i]*ll[i]
    if not check(x): flg = False

print("YES" if flg else "NO")