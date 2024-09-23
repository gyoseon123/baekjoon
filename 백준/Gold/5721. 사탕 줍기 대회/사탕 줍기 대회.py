import sys
input = sys.stdin.readline

def find_max(line):
    if len(line) <= 2:
        return max(line)
    elif len(line) == 3:
        return max(line[1], line[0] + line[2])
    
    dp = [0]*len(line)
    dp[0] = line[0]
    dp[1] = line[1]
    dp[2] = line[0] + line[2]
    for i in range(3, len(line)):
        dp[i] = max(dp[i-2], dp[i-3]) + line[i]
    
    return max(dp)

while True:
    n,m = map(int, input().split())
    if (n,m) == (0,0): break
    
    board = [list(map(int, input().split())) for _ in range(n)]
    l = [0]*n
    
    for i in range(n):
        l[i] = find_max(board[i])
    
    if len(l) <= 2:
        print(max(l))
        continue
    elif len(l) == 3:
        print(max(l[1], l[0] + l[2]))
        continue
    
    dp = [0]*n
    dp[0] = l[0]
    dp[1] = l[1]
    dp[2] = l[0] + l[2]
    
    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3]) + l[i]
    
    print(max(dp))
    
    
    