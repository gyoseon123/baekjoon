import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,l,k = map(int, input().split())
    arr = []
    right = []
    left = []
    for i in range(n):
        p,a = map(int, input().split())
        arr.append((p,a))
        if a > 0:
            right.append(p)
        else:
            left.append(p)
    
    arr.sort()
    right.sort()
    left.sort()

    result = []

    nright = 0
    nleft = len(left)
    for i in range(n):
        # print(i, nright, nleft)
        if arr[i][1] > 0:
            if nright < nleft:
                result.append((left[len(left) - nleft + nright]+1, arr[i][1]))
            else:
                result.append((l-right[nright - nleft]+1, arr[i][1]))
            nright += 1
        else:
            if nright < nleft:
                result.append((left[len(left) - nleft + nright]+1, arr[i][1]))
            else:
                result.append((l-right[nright - nleft]+1, arr[i][1]))
            nleft -= 1

    result.sort()
    # print(result)
    print(result[k-1][1])