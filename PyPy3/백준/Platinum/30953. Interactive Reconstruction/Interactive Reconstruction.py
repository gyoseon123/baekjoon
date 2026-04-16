import sys
input = sys.stdin.readline

n = int(input())

p = 0
while n > 2**p: p += 1

print("QUERY", "1"*n, flush=True)
degree = list(map(int, input().split()))

leaf = []

for i in range(n):
    if degree[i] == 1: leaf.append(i)

qry = ["".join(["1" if x&(1<<j) else "0" for x in range(n)]) for j in range(p)]
query = []

for q in qry:
    print("QUERY", q, flush=True)
    query.append(list(map(int, input().split())))

ans = []

while leaf:
    x = leaf.pop()
    y = sum([2**i for i in range(p) if query[i][x]])
    if degree[x] != 1: continue
    # print(x,y)
    ans.append((x,y))
    for i in range(p): query[i][y] -= int(qry[i][x])
    degree[x] -= 1
    degree[y] -= 1
    if (degree[y] == 1): leaf.append(y)

print("ANSWER", flush=True)
for x,y in ans:
    print(x+1, y+1, flush=True)