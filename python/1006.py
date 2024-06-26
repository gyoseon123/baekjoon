import sys
input = sys.stdin.readline

t = int(input())
inf = int(1e9)

for _ in range(t):    
    n,w = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l = [0] + l1 + l2
    
    if n == 1:
        if l[1] + l[2] <= w:
            print(1)
        else:
            print(2)
        continue
    
    m = inf

    dp = [[inf]*3 for _ in range(n+1)] #dp[i][0] = i번째에 위에만 채움 dp[i][1] = i번째에 아래만 채움 dp[i][2] = i번째에 위아래 다 채움

    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0

    dp[1][0] = 1
    dp[1][1] = 1
    if l[1] + l[n+1] <= w:
        dp[1][2] = 1
    else:
        dp[1][2] = 2
    
    for i in range(2,n+1):
        if l[i] + l[i-1] <= w:
            dp[i][0] = dp[i-1][1] + 1
        dp[i][0] = min(dp[i][0], dp[i-1][2] + 1)

        if l[i+n] + l[i+n-1] <= w:
            dp[i][1] = dp[i-1][0] + 1
        dp[i][1] = min(dp[i][1], dp[i-1][2] + 1)

        if l[i] + l[i+n] <= w:
            dp[i][2] = dp[i-1][2] + 1
        else:
            dp[i][2] = dp[i-1][2] + 2
        
        if l[i] + l[i-1] <= w and l[i+n] + l[i+n-1] <= w:
            dp[i][2] = min(dp[i][2], dp[i-2][2] + 2)
        dp[i][2] = min(dp[i][2], dp[i][0] + 1, dp[i][1] + 1)

    m = min(m, dp[n][2])



    # n+1 하고 n*2 구역 합침
    if l[n+1] + l[n*2] <= w:
        dp = [[inf]*3 for _ in range(n+1)] #dp[i][0] = i번째에 위에만 채움 dp[i][1] = i번째에 아래만 채움 dp[i][2] = i번째에 위아래 다 채움
    
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 2
        
        if l[1] + l[2] <= w:
            dp[2][0] = dp[1][1] + 1
        else:
            dp[2][0] = dp[1][2] + 1
        dp[2][1] = 3
        if l[2] + l[2+n] <= w:
            dp[2][2] = 3
        dp[2][2] = min(dp[2][2], dp[2][0] + 1) 
    
        for i in range(3,n+1):
            if l[i] + l[i-1] <= w:
                dp[i][0] = dp[i-1][1] + 1
            dp[i][0] = min(dp[i][0], dp[i-1][2] + 1)
    
            if l[i+n] + l[i+n-1] <= w:
                dp[i][1] = dp[i-1][0] + 1
            dp[i][1] = min(dp[i][1], dp[i-1][2] + 1)
    
            if l[i] + l[i+n] <= w:
                dp[i][2] = dp[i-1][2] + 1
            else:
                dp[i][2] = dp[i-1][2] + 2
            
            if l[i] + l[i-1] <= w and l[i+n] + l[i+n-1] <= w:
                dp[i][2] = min(dp[i][2], dp[i-2][2] + 2)
            dp[i][2] = min(dp[i][2], dp[i][0] + 1, dp[i][1] + 1)
    
        m = min(m, dp[n][0])

    
    #1구역하고 n구역 합침
    if l[1] + l[n] <= w:
        dp = [[inf]*3 for _ in range(n+1)] #dp[i][0] = i번째에 위에만 채움 dp[i][1] = i번째에 아래만 채움 dp[i][2] = i번째에 위아래 다 채움
    
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 2
        
        if l[n+1] + l[n+2] <= w:
            dp[2][1] = dp[1][0] + 1
        else:
            dp[2][1] = dp[1][2] + 1

        dp[2][0] = 3

        if l[2] + l[2+n] <= w:
            dp[2][2] = 3
        dp[2][2] = min(dp[2][2], dp[2][1] + 1) 
    
        for i in range(3,n+1):
            if l[i] + l[i-1] <= w:
                dp[i][0] = dp[i-1][1] + 1
            dp[i][0] = min(dp[i][0], dp[i-1][2] + 1)
    
            if l[i+n] + l[i+n-1] <= w:
                dp[i][1] = dp[i-1][0] + 1
            dp[i][1] = min(dp[i][1], dp[i-1][2] + 1)
    
            if l[i] + l[i+n] <= w:
                dp[i][2] = dp[i-1][2] + 1
            else:
                dp[i][2] = dp[i-1][2] + 2
            
            if l[i] + l[i-1] <= w and l[i+n] + l[i+n-1] <= w:
                dp[i][2] = min(dp[i][2], dp[i-2][2] + 2)
            dp[i][2] = min(dp[i][2], dp[i][0] + 1, dp[i][1] + 1)
    
        m = min(m, dp[n][1])
    
    if l[1] + l[n] <= w and l[n+1] + l[n*2] <= w:
        dp = [[inf]*3 for _ in range(n+1)] #dp[i][0] = i번째에 위에만 채움 dp[i][1] = i번째에 아래만 채움 dp[i][2] = i번째에 위아래 다 채움
    
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 2
        
        dp[2][0] = 3
        dp[2][1] = 3

        if l[2] + l[2+n] <= w:
            dp[2][2] = 3
        else:
            dp[2][2] = 4
    
        for i in range(3,n+1):
            if l[i] + l[i-1] <= w:
                dp[i][0] = dp[i-1][1] + 1
            dp[i][0] = min(dp[i][0], dp[i-1][2] + 1)
    
            if l[i+n] + l[i+n-1] <= w:
                dp[i][1] = dp[i-1][0] + 1
            dp[i][1] = min(dp[i][1], dp[i-1][2] + 1)
    
            if l[i] + l[i+n] <= w:
                dp[i][2] = dp[i-1][2] + 1
            else:
                dp[i][2] = dp[i-1][2] + 2
            
            if l[i] + l[i-1] <= w and l[i+n] + l[i+n-1] <= w:
                dp[i][2] = min(dp[i][2], dp[i-2][2] + 2)
            dp[i][2] = min(dp[i][2], dp[i][0] + 1, dp[i][1] + 1)
    
        m = min(m, dp[n-1][2])
    

    print(m)
