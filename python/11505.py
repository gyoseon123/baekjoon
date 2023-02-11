import sys
input = sys.stdin.readline

MOD = 1000000007
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = (init(node*2, start, (start+end)//2) * init(node*2+1, (start+end)//2+1, end))%MOD
        return tree[node]

def multiple_query(node, start, end, left, right):
    if start > right or end < left:
        return 1
    
    if start >= left and end <= right:
        return tree[node]
    
    return (multiple_query(node*2, start, (start+end)//2, left, right) * multiple_query(node*2+1, (start+end)//2+1, end, left, right))%MOD

def update_query(node, start, end, index, c):
    if start > index or index > end:
        return tree[node]

    if start == end:
        tree[node] = c
        return tree[node]
    
    tree[node] = (update_query(node*2, start, (start+end)//2, index, c) * update_query(node*2+1, (start+end)//2+1, end, index, c))%MOD
    return tree[node]

n,m,k = map(int, input().split())
tree = [0] * 4000000
l = [int(input()) for _ in range(n)]
init(1,0,n-1)
for _ in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        update_query(1,0,n-1,b-1,c)
    if a == 2:
        print(multiple_query(1,0,n-1,b-1,c-1)%MOD)