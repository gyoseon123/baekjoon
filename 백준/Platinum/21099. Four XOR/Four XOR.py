from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

flg = 0

if n <= 100:
    for l in combinations(a, 4):
        x = 0
        for i in l:
            x ^= i
        if x == 0:
            flg = 1
            break
else:
    flg = 1

print("Yes" if flg else "No")