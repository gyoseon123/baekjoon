import sys
input = sys.stdin.readline
board = [[0]*101 for _ in range(101)]
for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            board[j][k] = 1
print(sum(i.count(1) for i in board))