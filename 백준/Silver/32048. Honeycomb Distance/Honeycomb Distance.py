import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    a,b = map(int, input().split())
    if (a*b < 0):
        print(min(abs(a), abs(b)) + abs((abs(a) - abs(b))))
    else:
        print(abs(a)+abs(b))