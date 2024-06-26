import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]&1
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
    
def update(node, start, end, index, diff):
    if start <= index and index <= end:
        tree[node] += diff
        if start != end:
            update(node*2, start, (start+end)//2, index, diff)
            update(node*2+1, (start+end)//2+1, end, index, diff)

def solve(node, start, end, left, right):
    if right < start or left > end:
        return 0
    
    if start >= left and right >= end:
        return tree[node]
    
    return solve(node*2, start, (start+end)//2, left, right) + solve(node*2+1, (start+end)//2+1, end, left, right)


n = int(input())
arr = list(map(int, input().split()))
tree = [0]*400000
init(1,0,n-1)
m = int(input())
for _ in range(m):
    q,l,r = map(int, input().split())
    if q == 1:
        if arr[l-1]&1 != r&1:
            update(1,0,n-1,l-1,(r&1)-(arr[l-1]&1))
            arr[l-1] = r
    elif q == 2:
        print(r-l+1-solve(1,0,n-1,l-1,r-1))
    else:
        print(solve(1,0,n-1,l-1,r-1))
