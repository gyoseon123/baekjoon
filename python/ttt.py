import sys
input = sys.stdin.readline

r,c = map(int, input().split())
n = int(input())
h = list(map(int, input().split()))

board = [[0]*c for _ in range(r)]

h.sort(reverse=True)

cnt = 0

for i in range(r):
    for j in range(c):
        while i > 0 and cnt < n and board[i-1][j] == h[cnt]:
            cnt += 1
        
        if cnt == n:
                break

        board[i][j] = h[cnt]
        cnt += 1

        if cnt == n:
            break
    else:
        continue
    break

ans = 0
for j in range(c):
    for i in range(r-1, 0, -1):
        if board[i-1][j] > board[i][j]:
            ans += 1

print(ans)
        

