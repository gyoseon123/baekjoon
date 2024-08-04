import sys
input = sys.stdin.readline

def f(num, x1, x2):
    left = 0
    right = x1+x2+1
    while left + 1 < right:
        mid = (left+right)//2
        if mid <= x1:
            if num*mid <= m:
                left = mid
            else:
                right = mid
        else:
            if num*mid + (mid - x1) <= m:
                left = mid
            else:
                right = mid

    return min(num*left + x2, m)


t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    l = []
    for i in range(n):
        l.append((a[i], c[i]))
    l.sort()
    ans = 0
    for i in range(n-1): # 마지막 인덱스는 마지막에 처리할 것
        if l[i][0] + 1 == l[i+1][0]:
            ans = max(ans, f(l[i][0], l[i][1], l[i+1][1]))
        else:
            ans = max(ans, f(l[i][0], l[i][1], 0))
    
    ans = max(ans, f(l[n-1][0],l[n-1][1], 0))
    
    print(ans)