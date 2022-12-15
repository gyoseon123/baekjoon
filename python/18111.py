import sys
input = sys.stdin.readline
n,m,b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
inven = b
result = []
least = 1e9
index = 0
def check_block(target):
    global least
    global index
    put = 0
    out = 0
    for i in range(n):
        for j in range(m):
            dif = graph[i][j] - target
            if dif > 0:
                out += dif
            else:
                put += abs(dif)
    cost = put + out*2
    if out + inven >= put and cost <= least:
        index = target
        least = cost



for i in range(257):
    check_block(i)
print(least, index)