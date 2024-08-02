from itertools import permutations

words = [input() for _ in range(6)]
ans = []

for p in permutations(words, 6):
    board = [list(p[0]), list(p[1]), list(p[2])]
    rot_board = list(zip(*board))

    flg = True
    for i in range(3):
        if rot_board[i] != tuple(p[i+3]):
            flg = False
            break
    
    if flg:
        ans.append(board)

ans.sort()
if ans:
    answer = ans[0]
else:
    print(0)
    exit()

for i in range(3):
    for j in range(3):
        print(answer[i][j], end='')
    print()
