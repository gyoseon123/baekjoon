def dfs(x):
    if visited[x] == 0:
        visited[x] = 1
        l1.add(x)
        l2.add(len2[x-1])
        comp.append(x)
        dfs(len2[x-1])

n = int(input())
len1 = list(range(1,n+1))
len2 = [int(input()) for _ in range(n)]
visited = [0]*(n+1)
result = []
for i in range(1,n+1):
    comp = []
    l1 = set()
    l2 = set()
    dfs(i)
    if l1 == l2:
        for j in l1:
            result.append(j)
    else:
        for j in comp:
            visited[j] = 0
print(len(result))
result.sort()
for i in result:
    print(i)