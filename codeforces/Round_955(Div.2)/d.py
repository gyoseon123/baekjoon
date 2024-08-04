import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a,b = b, a%b
    return a

t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    is_not_snow = [input().rstrip() for _ in range(n)]
    snow = 0
    not_snow = 0
    for i in range(n):
        for j in range(m):
            if is_not_snow[i][j] == "1":
                not_snow += board[i][j]
            else:
                snow += board[i][j]
    
    comb = set()
    for i in range(n-k+1):
        for j in range(m-k+1):
            ns = 0
            s = 0
            for x in range(k):
                for y in range(k):
                    if is_not_snow[i+x][j+y] == "1":
                        ns += 1
                    else:
                        s += 1
            comb.add((s,ns))
    
    comb = list(comb)

    up = []
    down = []
    for x,y in comb:
        if x > y:
            up.append(x - y)
        else:
            down.append(y - x)
    
    gcd1, gcd2 = -1,-1
    if up and up[0] != 0:
        gcd1 = up[0]
    if down and down[0] != 0:
        gcd2 = down[0]
    
    for i in range(1, len(up)):
        if up[i] != 0:
            gcd1 = gcd(gcd1, up[i])
        
    for i in range(1, len(down)):
        if down[i] != 0:
            gcd2 = gcd(gcd2, down[i])

    # print(up, down)
    # print(gcd1, gcd2)
    # print(snow, not_snow)

    if snow == not_snow:
        print("YES")
        continue

    if snow > not_snow and gcd1 != -1:
        if (snow - not_snow)%gcd1 == 0:
            print("YES")
            continue

    if snow < not_snow and gcd2 != -1:
        if (not_snow - snow)%gcd2 == 0:
            print("YES")
            continue
    
    print("NO")
        


    

    
    

    


