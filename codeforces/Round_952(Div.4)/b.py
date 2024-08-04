t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for x in range(2, n+1):
        a = 0
        for i in range(1, 10000):
            if x*i <= n:
                a += x*i
            else:
                b = x
                break
        if ans < a:
            ans = max(ans, a)
            ret = b
    print(ret)
