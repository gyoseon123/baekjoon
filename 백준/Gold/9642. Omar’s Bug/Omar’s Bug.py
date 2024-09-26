import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,x,y = map(int, input().split())
    
    if y == 1:
        cnt = 0
        for i in range(1, 101):
            if i != x:
                print(i, end=' ')
            else:
                cnt -= 1
                
            cnt += 1
            if cnt == n:
                break
        print()
    else:
        for i in range(1, n):
            print(i, end=' ')
            
        if x <= n:
            print(n)
        else:
            print(x)