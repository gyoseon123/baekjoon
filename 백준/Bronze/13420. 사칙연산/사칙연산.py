import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l, r = input().split("=")
    if eval(l) == int(r):
        print("correct")
    else:
        print("wrong answer")