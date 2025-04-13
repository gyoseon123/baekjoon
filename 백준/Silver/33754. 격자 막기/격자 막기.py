import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

s = sum(map(sum, a))

if s == n*2:
    print(2)
    exit()

flg = 0
for i in range(n-1):
    if a[0][i] == 0 and a[1][i+1] == 0: flg = 1
    if a[1][i] == 0 and a[0][i+1] == 0: flg = 1

for i in range(n):
    if a[0][i] == 0 and a[1][i] == 0: flg = 1

print(0 if flg else 1)