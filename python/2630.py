import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white,blue = 0,0


def divide_paper(n,board):
    global white,blue
    cnt = sum([i.count(1) for i in board])
    if cnt == n*n:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        divide_paper(n//2,[k[0:n//2] for k in board[0:n//2]])
        divide_paper(n//2,[k[0:n//2] for k in board[n//2:n]])
        divide_paper(n//2,[k[n//2:n] for k in board[0:n//2]])
        divide_paper(n//2,[k[n//2:n] for k in board[n//2:n]])
divide_paper(n,paper)
print(white, blue, sep = '\n')