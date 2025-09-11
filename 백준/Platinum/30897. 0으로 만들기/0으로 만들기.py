import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = {}
op = []

d[0] = -1
summ = 0
start, end = -1, -1
for i in range(n):
    if summ >= 0:
        op.append('-')
        summ -= a[i]
        if summ in d:
            start = d[summ]+1
            end = i
            break
        d[summ] = i
    else:
        op.append('+')
        summ += a[i]
        if summ in d:
            start = d[summ]+1
            end = i
            break
        d[summ] = i

rev = 0
if op[start] == "-":
    rev = 1


print("YES")
# print(start, end)
# print(op)

for i in range(n):
    if i == start:
        print("(", end='')
    
    if start <= i < end:
        print(a[i], end='')
        if rev: print('+' if op[i+1] == '-' else '-', end='')
        else: print('+' if op[i+1] == '+' else '-', end='')
        continue
    
    if i == end:
        print(a[i], end='')
        print(')', end='')
        if i != n-1:
            print("*", end='')
        continue
    
    if i == n-1:
        print(a[i])
        break
    
    print(a[i], end='')
    print('*', end='')