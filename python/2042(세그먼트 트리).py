import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
    
def sum_query(node, start, end, left, right):
    if right < start or left > end:
        return 0
    
    if start >= left and end <= right:
        return tree[node]
    
    return sum_query(node*2, start, (start+end)//2, left, right) + sum_query(node*2+1, (start+end)//2+1, end, left, right)

def update_query(node, start, end, index, diff):
    if start <= index and index <= end:
        tree[node] += diff
        if start != end:
            update_query(node*2, start, (start+end)//2, index, diff)
            update_query(node*2+1, (start+end)//2+1, end, index, diff)


n,m,k = map(int, input().split())
tree = [0] * 2000000
l = [int(input()) for _ in range(n)]
init(1,0,n-1)
for _ in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        diff = c - l[b-1] 
        l[b-1] = c
        update_query(1,0,n-1,b-1, diff)
    if a == 2:
        print(sum_query(1,0,n-1,b-1,c-1))