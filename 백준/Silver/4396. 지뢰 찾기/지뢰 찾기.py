import sys
input = sys.stdin.readline

n = int(input())
board1 = [input().rstrip() for _ in range(n)]
board2 = [input().rstrip() for _ in range(n)]

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]

open = False
for i in range(n):
    for j in range(n):
        if board2[i][j] == "x" and board1[i][j] == "*":
            open = True

for i in range(n):
    for j in range(n):
        if open and board1[i][j] == "*":
            print("*", end="")
        elif board2[i][j] == "x":
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if (0 <= nx < n) and (0 <= ny < n) and board1[nx][ny] == "*":
                    cnt += 1
            print(cnt, end='')
        else:
            print(".", end='')
    print()