import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
n,k = map(int, input().split())
score = []
for i in range(n):
    w,s,e = map(int, input().split())
    if w != 5:
        score.append((w,s,e))

ans = 0
def dfs(i,csum,visited):
    global ans
    if i == len(score):
        if csum == k:
            ans += 1
        return 
    now = score[i]
    flag = False
    for a in visited:
        if now[0] == score[a][0] and now[2] >= score[a][1] and now[1] <= score[a][2]:
            flag = True
    if not flag:
        x = score[i][2] - score[i][1] + 1 
        dfs(i+1, csum+x, visited + [i])
    dfs(i+1, csum, visited)    


dfs(0,0, [])
print(ans)
