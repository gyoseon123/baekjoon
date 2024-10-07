import sys
input = sys.stdin.readline

def sum_q(node, start, end, left, right):
    if left <= start and end <= right: return tree[node]
    if right < start or end < left: return 0
    mid = (start+end)//2
    return sum_q(node*2, start, mid, left, right) + sum_q(node*2+1, mid+1, end, left, right)

def update_q(node, start, end, idx, diff):
    if start <= idx <= end:
        tree[node] += diff
        if start != end:
            mid = (start+end)//2
            update_q(node*2, start, mid, idx, diff)
            update_q(node*2+1, mid+1, end, idx, diff)
    

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bb = [0]*1000001
tree = [0]*(4*n)

for i in range(n):
    bb[b[i]] = i

arr = []
for i in range(n):
    arr.append((bb[a[i]], i))

arr.sort()
ans = 0

for i in range(n):
    now, idx = arr[i]
    ans += sum_q(1, 0, n-1, idx+1, n-1)
    update_q(1, 0, n-1, idx, 1)
    
print(ans)