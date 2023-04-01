import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)]
parent = [i for i in range(g+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[b] = a

ans = 0
for plane in arr:
    f = find(plane)
    if f == 0:
        break
    union(f-1, f)
    ans += 1

print(ans)