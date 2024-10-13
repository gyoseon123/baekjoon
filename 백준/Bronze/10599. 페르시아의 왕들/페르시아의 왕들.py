import sys
input = sys.stdin.readline

while True:
    a,b,c,d = map(int, input().split())
    if (a,b,c,d) == (0,0,0,0): break
    
    print(c - b, d - a)