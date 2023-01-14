import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

city = [list(map(int, input().split())) for _ in range(n)]
info = list(map(int, input().split()))
parent = [i for i in range(n+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return 
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(1,n+1):
    for j in range(1,n+1):
        if city[i-1][j-1] == 1:
            union(i,j)

check = set([find(i) for i in info])

if len(check) <= 1:
    print('YES')
else:
    print('NO')