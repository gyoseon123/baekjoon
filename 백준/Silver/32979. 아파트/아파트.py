import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
apart = list(map(int, input().split()))
qry = list(map(int, input().split()))

now = 0

for i in range(t):
    now += qry[i]-1
    now %= (n*2)
    print(apart[now], end=' ')