import sys
input = sys.stdin.readline

t = int(input())


def solve():
    f = int(input())
    rank = {}
    relation = {}

    def find(x):
        if x not in relation:
            relation[x] = x
            rank[x] = 1
        if relation[x] != x:
            relation[x] = find(relation[x])
        return relation[x]
            
    def union(a,b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        
        if a > b:
            relation[a] = b
            rank[b] += rank[a] 
        else:
            relation[b] = a
            rank[a] += rank[b]

    for _ in range(f):
        a,b = input().rstrip().split()
        union(a,b)
        print(rank[find(min(a,b))])

for i in range(t):
    solve()