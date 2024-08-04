import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    if -abs(x) <= y - abs(x) + 1:
        print("YES")
    else:
        print("NO")