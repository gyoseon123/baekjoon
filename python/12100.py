from collections import deque
import sys
import copy
input = sys.stdin.readline
n = int(input()) 
board = [list(map(int, input().split())) for _ in range(n)]
result = []
def right():
    for i in range(n):
        for j in range(n-1,0,-1):
            if board[i][j] == 0:
                while board[i][j] == 0:
                    l = deque(board[i][:j+1])
                    if l.count(0) == len(l):
                        break
                    l.rotate(1)
                    board[i] = list(l) + board[i][j+1:]
        for j in range(n-1,0,-1):
            if board[i][j-1] == board[i][j]:
                board[i][j] *= 2
                board[i][j-1] = 0
        for j in range(n-1,0,-1):
            if board[i][j] == 0:
                while board[i][j] == 0:
                    l = deque(board[i][:j+1])
                    if l.count(0) == len(l):
                        break
                    l.rotate(1)
                    board[i] = list(l) + board[i][j+1:]

def left():
    for i in range(n):
        for j in range(n-1):
            if board[i][j] == 0:
                while board[i][j] == 0:
                    l = deque(board[i][j:])
                    if l.count(0) == len(l):
                        break
                    l.rotate(-1)
                    board[i] = board[i][:j] + list(l)
        for j in range(n-1):
            if board[i][j+1] == board[i][j]:
                board[i][j] *= 2
                board[i][j+1] = 0
        for j in range(n-1):
            if board[i][j] == 0:
                while board[i][j] == 0:
                    l = deque(board[i][j:])
                    if l.count(0) == len(l):
                        break
                    l.rotate(-1)
                    board[i] = board[i][:j] + list(l)

def up():
    global board
    n_board = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_board[i].append(board[j][i])
    board = n_board
    left()
    n_board = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_board[j].append(board[i][j])
    board = n_board

def down():
    global board
    n_board = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_board[i].append(board[j][i])
    board = n_board
    right()
    n_board = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_board[j].append(board[i][j])
    board = n_board

def check_max():
    max = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > max:
                max = board[i][j]
    return max


def game(arr):
    for i in arr:
        if i == 0:
            left()
        if i == 1:
            right()
        if i == 2:
            up()
        if i == 3:
            down()            

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    temp = copy.deepcopy(board)
                    game([a,c,b,d,e])
                    result.append(check_max())
                    board = copy.deepcopy(temp)


print(max(result))












# 개선된 풀이
# import sys
# import copy
# input = sys.stdin.readline
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]


# def right():
#     for line in board:
#         now = n-1
#         point = now-1
#         while point >= 0:
#             if line[now] == 0:
#                 line[now] = line[point]
#                 line[point] = 0
#                 point -= 1
#             elif now == point:
#                 point -= 1
#             elif line[now] != line[point]:
#                 if line[point] == 0:
#                     point -= 1
#                 else:
#                     now -= 1
#             else:
#                 line[now] *= 2
#                 line[point] = 0
#                 now -= 1
#                 point -= 1

# def left():
#     for line in board:
#         now = 0
#         point = 1
#         while point < n:
#             if line[now] == 0:
#                 line[now] = line[point]
#                 line[point] = 0
#                 point += 1
#             elif now == point:
#                 point += 1
#             elif line[now] != line[point]:
#                 if line[point] == 0:
#                     point += 1
#                 else:
#                     now += 1
#             else:
#                 line[now] *= 2
#                 line[point] = 0
#                 now += 1
#                 point += 1

# def up():
#     global board
#     board = list(map(list, zip(*board[::-1])))
#     right()
#     board = list(map(list, zip(*board)))[::-1]

# def down():
#     global board
#     board = list(map(list, zip(*board[::-1])))
#     left()
#     board = list(map(list, zip(*board)))[::-1]

# def game(arr):
#     for i in arr:
#         if i == 0:
#             right()
#         if i == 1:
#             left()
#         if i == 2:
#             up()
#         if i == 3:
#             down()

# result = []

# def find_max(arr):
#     max = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] > max:
#                 max = arr[i][j]
#     result.append(max)


# for a in range(4):
#     for b in range(4):
#         for c in range(4):
#             for d in range(4):
#                 for e in range(4):
#                     temp = copy.deepcopy(board)
#                     game([a,b,c,d,e])
#                     find_max(board)
#                     board = copy.deepcopy(temp)


# print(max(result))