import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x,y,k = map(int, input().split())
    ans = 0
    while x > 1:
        rem = y - x%y
        if k >= rem:
            x += rem
            while x%y == 0:
                x //= y
            k -= rem
        else:
            break

    
    if x == 1:
        if k >= y:
            k = k%(y-1)
        if x + k == y:
            print(1)
        else:
            print(x + k)
    else:
        print(x + k)
            
    
            
            
