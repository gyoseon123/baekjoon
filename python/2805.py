def search_len(array, n):
    count = 0
    for i in array:
        if i > n:
            count += (i - n)
    return count

a,b = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
print(tree, start, end)
while True:
    mid = (start+end)//2
    temp = search_len(tree,mid)
    print(start,end,temp)
    if temp == b:
        print(mid)
        break
    elif temp > b:
        start = mid+1
    else:
        end = mid-1
    
