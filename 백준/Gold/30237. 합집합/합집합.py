import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = [set(list(map(int, input().split()))[1:]) for _ in range(n)]
    ans = 0
    
    alls = set()
    for s in l:
        alls |= s
    
    for i in range(1, 51):
        now = set()
        for s in l:
            if i not in s:
                now |= s
        
        if now != alls:
            ans = max(ans, len(now))
    
    print(ans)