import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(max([l[i] for i in range(0, n, 2)]))