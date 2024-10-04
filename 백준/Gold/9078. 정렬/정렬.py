import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans = sorted(l[:])
    
    for target in range(n, 0, -1):
        idx = l.index(target)
        itv = n - idx - 1
        if itv < 0: break
        
        if itv%2 == 0:
            l = l[:idx] + l[idx+1:idx + (itv//2)*2+1] + [target] + l[idx + (itv//2)*2+1:]
        else:
            l = l[:idx] + l[idx+1:idx + (itv//2)*2+1] + [target] + l[idx + (itv//2)*2+1:]
            if n >= 3: l = l[:n-3] + [l[n-1]] + l[n-3:n-1] + l[n:]
        n -= 1

            
    print("YES" if ans == l else "NO")