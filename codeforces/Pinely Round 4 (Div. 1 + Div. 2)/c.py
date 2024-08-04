import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a.count(0) == n:
        print(0)
        print()
        continue

    res = []

    flag = False

    for i in range(40):
        a.sort()
        if n&1:
            mid = a[n//2]
        else:
            mid1 = a[n//2]
            mid2 = a[n//2-1]
            if (mid1 + mid2)%2 != 0:
                break
            else:
                mid = (mid1 + mid2)//2
    
        s = set(a)
        if len(s) == 2:
            if sum(s)%2 == 0 and i < 38 and abs(list(s)[0] - list(s)[1])%2 == 0:
                flag = True
                res.append(sum(s)//2)
                res.append(abs(list(s)[0] - sum(s)//2))
                print(len(res))
                print(*res)
                break

        res.append(mid)
        cnt = 0
        for j in range(n):
            a[j] = abs(a[j] - mid)
            if a[j] == 0:
                cnt += 1

        if cnt == n:
            flag = True 
            print(i+1)
            print(*res)
            break

    if not flag:
        print(-1)

        
