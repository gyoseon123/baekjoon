# n,m = map(int, input().split())
# r,c,d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# def clean(x,y,state): # state: 0 - 위 1 - 오른쪽 2 - 아래 3 - 왼쪽
#     global cnt
#     graph[x][y] = 2
#     cnt += 1
#     for i in range(1,5):
#         a = (i+state)%4
#         if a == 0:
    
