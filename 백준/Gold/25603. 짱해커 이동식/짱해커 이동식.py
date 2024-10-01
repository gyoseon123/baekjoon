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

n,k = map(int, input().split())
a = list(map(int, input().split()))

tree = [0]*(n*4)
init(1, 0, n-1)
ans = -1

for i in range(n-k+1):
    ans = max(ans, min_query(1, 0, n-1, i, i+k-1))

print(ans)