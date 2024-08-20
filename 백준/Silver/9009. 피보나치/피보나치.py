fib = [0,1]
for i in range(43):
    fib.append(fib[-2] + fib[-1])

t = int(input())
for _ in range(t):
    n = int(input())
    val = 0
    res = []
    for i in range(44, 0, -1):
        if val + fib[i] <= n:
            val += fib[i]
            res.append(fib[i])
        
        if val == n:
            break
    
    print(*res[::-1])

