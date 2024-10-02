import sys
input = sys.stdin.readline

n = int(input())

div = [-1]*5000001

div[1] = 1

for i in range(2, len(div)):
    if div[i] == -1:
        for j in range(i, len(div), i):
            if div[j] == -1:
                div[j] = i

l = list(map(int, input().split()))

for num in l:
    now = div[num]
    res = []
    while now != 1:
        res.append(now)
        num //= now
        now = div[num]

    print(*res)