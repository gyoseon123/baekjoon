import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    odd = []
    even = []

    for i in l:
        if i&1:
            odd.append(i)
        else:
            even.append(i)

    if len(odd) == 0 or len(even) == 0:
        print(0)
        continue

    odd.sort()
    even.sort()

    max_odd = odd[-1]
    max_even = even[-1]
    cnt = 0
    for num in even:
        if num < max_odd:
            cnt += 1
            max_odd += num
        else:
            max_odd = max_odd + max_even
            max_odd += num
            cnt += 2
    print(cnt)


