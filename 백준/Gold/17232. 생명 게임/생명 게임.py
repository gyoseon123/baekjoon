import sys
input = sys.stdin.readline

def find_board_sum():
    ret = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i-1][j-1] == "*":
                ret[i][j] = 1
    
    for i in range(1,n+1):
        for j in range(1,m):
            ret[i][j+1] += ret[i][j]

    for j in range(1,m+1):
        for i in range(1,n):
            ret[i+1][j] += ret[i][j]
    
    return ret

def find_board_val(x1, y1, x2, y2):
    return board_sum[x2][y2] - board_sum[x2][y1-1] - board_sum[x1-1][y2] + board_sum[x1-1][y1-1]

n,m,t = map(int, input().split())
k,a,b = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

for _ in range(t):
    board_sum = find_board_sum()
    for i in range(1,n+1):
        for j in range(1,m+1):
            life = find_board_val(max(1, i - k), max(1, j - k), min(n, i + k), min(m, j + k))
            if board[i-1][j-1] == "*":
                if life - 1 < a:
                    board[i-1][j-1] = "."
                if life - 1 > b:
                    board[i-1][j-1] = "."
            else:
                if a < life <= b:
                    board[i-1][j-1] = "*"

for line in board:
    print(*line, sep='')
