import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    rot_board = list(zip(*board[::-1]))

    row = []
    col = []
    for i in range(n):
        if len(set(board[i])) == n:
            row.append(i)
        
    for i in range(n):
        if len(set(rot_board[i])) == n:
            col.append(i)
    
    print(max(len(row), len(col)))
    if len(row) >= len(col):
        for i in range(len(col)):
            target = (row[i], col[i])
            now = board[target[0]][target[1]]
            r = set(board[target[0]])
            c = set(rot_board[target[1]])
            ok = (r&c)^{now}
            print(target[0]+1, target[1]+1, list(ok)[0])
        
        rem = list(set([i for i in range(n)])^set(col))
        for i in range(len(col), len(row)):
            target = (row[i], rem[i - len(col)])
            now = board[target[0]][target[1]]
            r = set(board[target[0]])
            c = set(rot_board[target[1]])

            if len(r) <= n-2:
                ok = c^{now}
            elif len(c) <= n-2:
                ok = r^{now}
            else:
                ok = (r&c)^{now}
                
            print(target[0]+1, target[1]+1, list(ok)[0])
    else:
        for i in range(len(row)):
            target = (row[i], col[i])
            now = board[target[0]][target[1]]
            r = set(board[target[0]])
            c = set(rot_board[target[1]])
            ok = (r&c)^{now}
            print(target[0]+1, target[1]+1, list(ok)[0])
        
        rem = list(set([i for i in range(n)])^set(row))
        for i in range(len(row), len(col)):
            target = (rem[i - len(row)], col[i])
            now = board[target[0]][target[1]]
            r = set(board[target[0]])
            c = set(rot_board[target[1]])
  
            if len(r) <= n-2:
                ok = c^{now}
            elif len(c) <= n-2:
                ok = r^{now}
            else:
                ok = (r&c)^{now}

            print(target[0]+1, target[1]+1, list(ok)[0])

        