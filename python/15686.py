import sys
import itertools
input = sys.stdin.readline
n,m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
result = []
for i in range(n):
    for j in range(n):
        x = town[i][j]
        if x == 1:
            house.append([i,j])
        if x == 2:
            chicken.append([i,j])

for k in itertools.combinations(chicken, m):
    cnt = 0
    for i in house:
        m = int(1e5)
        for j in k:
            x = abs(i[0]-j[0]) + abs(i[1]-j[1])
            if x < m:
                m = x
        cnt += m
    result.append(cnt)
print(min(result))
