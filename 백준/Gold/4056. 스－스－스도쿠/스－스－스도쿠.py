import sys
input = sys.stdin.readline

def check_row(n):
    ret = set()
    for j in range(9):
        if board[n][j] in ret: return False
        if board[n][j] != 0: ret.add(board[n][j])
    return True

def check_col(n):
    ret = set()
    for i in range(9):
        if board[i][n] in ret: return False
        if board[i][n] != 0: ret.add(board[i][n])
    return True
    
def check_sq(x,y):
    ret = set()
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] in ret: return False
            if board[x+i][y+j] != 0: ret.add(board[x+i][y+j])
    return True

def dfs(cnt):
    if cnt == 5:
        res = True
        for i in range(9):
            res &= check_row(i)
            res &= check_col(i)
        for i in range(3):
            for j in range(3):
                res &= check_sq(i*3, j*3)
        if not res: return False
        
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        return True
    
    ret = False
    
    for i in range(1, 10):
        board[empty[cnt][0]][empty[cnt][1]] = i
        if check_row(empty[cnt][0]) and check_col(empty[cnt][1]) and check_sq(empty[cnt][0]//3*3, empty[cnt][1]//3*3):
            ret |= dfs(cnt+1)
    
    return ret

t = int(input())

for case in range(t):
    board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
    empty = []
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty.append((i,j))

    if not dfs(0):
        print("Could not complete this grid.")
    print()