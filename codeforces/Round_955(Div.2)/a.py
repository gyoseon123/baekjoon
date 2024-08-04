import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    if x1 < y1:
        if x2 >= y2:
            print("NO")
        else:
            print("YES")
    else:
        if x2 <= y2:
            print("NO")
        else:
            print("YES")