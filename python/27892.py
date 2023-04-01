x,n = map(int, input().split())
visited = {}
for i in range(n):
    visited[x] = i
    if x&1:
        x = (2*x)^6
    else:
        x = (x//2)^6
    if x in visited:
        rev_visited = {j:i for i,j in visited.items()}
        dif = i-visited[x]+1
        print(rev_visited)
        print(rev_visited[visited[x] + (n-i-1)%dif])
        break
else:
    print(x)