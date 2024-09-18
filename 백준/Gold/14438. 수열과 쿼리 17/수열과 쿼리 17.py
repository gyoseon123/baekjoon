import sys
input = sys.stdin.readline
INF = sys.maxsize

def init(node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    tree[node] = min(init(node*2, start, (start+end)//2), init(node*2+1, (start+end)//2+1, end))
    return tree[node]

def min_query(node, start, end, left, right):
    if right < start or end < left:
        return INF
    
    if left <= start and end <= right:
        return tree[node]
    
    return min(min_query(node*2, start, (start+end)//2, left, right), min_query(node*2+1, (start+end)//2+1, end, left, right))

def update_query(node, start, end, idx, val):
    if idx < start or end < idx:
        return tree[node]
    if start == end:
        tree[node] = val
        return tree[node]
    tree[node] = min(update_query(node*2, start, (start+end)//2, idx, val), update_query(node*2+1, (start+end)//2+1, end, idx, val))
    return tree[node]

n = int(input())
a = list(map(int, input().split()))

tree = [0]*(n*4)
init(1, 0, n-1)

m = int(input())
for _ in range(m):
    q, *qry = list(map(int, input().split()))
    if q == 1:
        update_query(1, 0, n-1, qry[0]-1, qry[1])
    else:
        print(min_query(1, 0, n-1, qry[0]-1, qry[1]-1))