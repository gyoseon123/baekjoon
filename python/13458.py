import sys
input = sys.stdin.readline
n = int(input())
ai = list(map(int, input().split()))
b,c = map(int, input().split())
cnt = 0
for i in ai:
    i -= b
    cnt += 1
    if i <= 0:
        continue
    if i%c == 0:
        cnt += i//c
    else:
        cnt += i//c + 1
print(cnt)