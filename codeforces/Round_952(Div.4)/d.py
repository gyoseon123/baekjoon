import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    

    max_n = 0
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if board[i][j] == "#":
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            max_n = i
        
    for i in range(m):
        if board[max_n][i] == "#":
            start = i
            break
    
    print(max_n+1, start + max_cnt//2 + 1)

    

