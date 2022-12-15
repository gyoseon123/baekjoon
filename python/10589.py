import sys
input = sys.stdin.readline

n,m = map(int, input().split())
if n == 1 and m == 1:
    print(0)
elif n&1 or m&1:
    print(n//2+m//2)
    for i in range(1,n,2):
        print(i+1,1,i+1,m)
        
    for i in range(1,m,2):
        print(1,i+1,n,i+1)
else:
    print((n+m)//2)
    for i in range(1,n,2):
        print(i+1,1,i+1,m)
        
    for i in range(1,m,2):
        print(1,i+1,n,i+1)
