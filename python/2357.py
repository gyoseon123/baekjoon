import sys
input = sys.stdin.readline

def init_min(node, start, end):
    if start == end:
        min_tree[node] = l[start]
        return min_tree[node]
    else:
        min_tree[node] = min(init_min(node*2, start, (start+end)//2), init_min(node*2+1, (start+end)//2+1, end))
        return min_tree[node]

def init_max(node, start, end):
    if start == end:
        max_tree[node] = l[start]
        return max_tree[node]
    else:
        max_tree[node] = max(init_max(node*2, start, (start+end)//2), init_max(node*2+1, (start+end)//2+1, end))
        return max_tree[node]

def find_min_query(node, start, end, left, right):
    if start > right or end < left:
        return INF
    
    if start >= left and end <= right:
        return min_tree[node]
    
    return min(find_min_query(node*2, start, (start+end)//2, left, right), find_min_query(node*2+1, (start+end)//2+1, end, left, right))

def find_max_query(node, start, end, left, right):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return max_tree[node]
    
    return max(find_max_query(node*2, start, (start+end)//2, left, right), find_max_query(node*2+1, (start+end)//2+1, end, left, right))



n,m = map(int, input().split())
l = [int(input()) for _ in range(n)]
INF = int(1e9)
max_tree = [0] * 400000
min_tree = [INF] * 400000
init_max(1, 0, n-1)
init_min(1, 0, n-1)

for _ in range(m):
    a,b = map(int, input().split())
    print(find_min_query(1,0,n-1,a-1,b-1), find_max_query(1,0,n-1,a-1,b-1))
