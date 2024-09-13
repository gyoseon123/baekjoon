import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
rot_board = list(zip(*board[::-1]))

row = 0
col = 0

for i in range(n):
    cnt = 0
    for j in range(m):
        if board[i][j] == "1":
            cnt += 1
    if cnt&1:
        row += 1

for i in range(m):
    cnt = 0
    for j in range(n):
        if rot_board[i][j] == "1":
            cnt += 1
    if cnt&1:
        col += 1

# print(row, col)
if (row&1) & (col&1):
    print(min(row + m - col, n - row + col))
elif (row&1) | (col&1) == 0:
    ans = min(row + col, n - row + m - col)
    print(ans)
else:
    print(-1)