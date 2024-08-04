import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    a = [list(map(int, list(input().strip()))) for _ in range(n)] 
    b = [list(map(int, list(input().strip()))) for _ in range(n)] 
    ar = list(zip(*a[::-1]))
    br = list(zip(*b[::-1]))

    flg = True
    for i in range(n):
        if (sum(a[i])%3 != sum(b[i])%3):
            print("NO")
            flg = False
            break
    
    if flg:
        for i in range(m):
            if (sum(ar[i])%3 != sum(br[i])%3):
                print("NO")
                flg = False
                break

    
    if flg:
        print("YES")
