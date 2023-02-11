from collections import deque
def merge_sort(l):
    size = len(l)
    if size == 1:
        return l
    mid = (size+1)//2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    merged = merge(left, right) 
    return merged

def merge(l1, l2):
    global ans
    l1,l2 = deque(l1), deque(l2)
    merged = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            ans.append(l1[0])
            merged.append(l1.popleft())
        else:
            ans.append(l2[0])
            merged.append(l2.popleft())
    if len(l1):
        ans += l1
        merged += l1
    if len(l2):
        ans += l2
        merged += l2
    return merged

ans = []
n,k = map(int, input().split())
l = list(map(int, input().split()))
merge_sort(l)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)
