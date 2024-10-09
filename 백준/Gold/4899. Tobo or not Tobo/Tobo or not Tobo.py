from collections import deque
import sys
input = sys.stdin.readline

def trans(arr):
    return "".join(arr)

def rot_r(p, board):
    board[0+p], board[1+p], board[3+p], board[4+p] = board[3+p], board[0+p], board[4+p], board[1+p]
    return board

def rot_l(p, board):
    board[0+p], board[1+p], board[3+p], board[4+p] = board[1+p], board[4+p], board[0+p], board[3+p]
    return board

def bfs(start):
    if start == answer: return 0
    ret = int(1e9)
    q = deque()
    q.append((start, 0))
    visited = set()
    visited.add(trans(start))
    while q:
        now, dis = q.popleft()

        for i in (0,1,3,4):
            r = rot_r(i, now[:])
            if trans(r) not in visited:
                if r == answer:
                    return dis+1
                visited.add(trans(r))
                q.append((r[:], dis+1))

            l = rot_l(i, now[:])
            if trans(l) not in visited:
                if l == answer:
                    return dis+1
                visited.add(trans(l))
                q.append((l[:], dis+1))

    return ret

t = 1
while True:
    test = input().rstrip()
    if test == "0000000000": break

    y = int(test[0])
    oboard = list(test[1:])
    ans = int(1e9)
    answer = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    b = bfs(oboard)

    if b <= y:
        print(f"{t}. {b}")
    else:
        print(f"{t}. -1")
    t += 1