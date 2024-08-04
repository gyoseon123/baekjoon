import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = [input().rstrip() for _ in range(2)]
    ans = 0
    for i in range(n-2):
        up = board[0][i] + board[0][i+1] + board[0][i+2]
        down = board[1][i] + board[1][i+1] + board[1][i+2]
        if up == "..." and down == "x.x":
            ans += 1
        if down == "..." and up == "x.x":
            ans += 1
    print(ans)
            