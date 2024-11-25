import sys
input = sys.stdin.readline

n = int(input())

if n <= 2:
    print(1)
elif n <= 5:
    print(2)
else:
    print(3)