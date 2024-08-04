import math

t = int(input())
for _ in range(t):
    x,y,z,k = map(int, input().split())
    
    ans = 0
    for a in range(1, x+1):
        for b in range(1, y+1):
            if k%(a*b) == 0:
                c = k//(a*b)
                if c > z:
                    continue
                
                ret = 1
                ret *= (x - a + 1)
                ret *= (y - b + 1)
                ret *= (z - c + 1)
                ans = max(ans, ret)
    print(ans)                
            
