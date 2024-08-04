import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    a.append(b[0])
    for i in range(n-2):
        a.append(b[i] | b[i+1])
    a.append(b[-1])

    flag = True
    for i in range(n-1):
        if a[i] & a[i+1] != b[i]:
            flag = False
            break

    if flag:
        print(*a)
    else:
        print(-1)
