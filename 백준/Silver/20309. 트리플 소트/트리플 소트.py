import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
flag = False
for i in range(1,n,2):
    if l[i]&1:
        flag = True
        break

if flag:
    print('NO')
else:
    print('YES')