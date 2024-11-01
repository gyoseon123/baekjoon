board = [input() for _ in range(8)]

ans = 0
for i in range(8):
    for j in range(8):
        if i&1 and j&1 and board[i][j] == "F": ans += 1
        if not i&1 and not j&1 and board[i][j] == "F": ans += 1

print(ans)