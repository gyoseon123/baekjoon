t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    time_to_build = list(map(int, input().split()))
    graph = [[] for _ in range(k)]
    for i in range(k):
        x,y = map(int, input().split())
        graph[x].append(y)
    goal = int(input())