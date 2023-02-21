import sys
input = sys.stdin.readline
n,m = map(int, input().split())
loved = []
graph = []
total_love = 0
for _ in range(m):
    a,b,c,d = map(int, input().split())
    total_love += c
    if d == 1:
        loved.append((c,a,b))
    else:
        graph.append((c,a,b))
graph.sort(reverse=True)
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for c,a,b in loved:
    ans += c
    union(a,b)

for c,a,b in graph:
    if find(a) != find(b):
        ans += c
        union(a,b)

print(total_love - ans)