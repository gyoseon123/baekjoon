import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
x = sum(l) + (n-1)*8

print(x//24, x%24)