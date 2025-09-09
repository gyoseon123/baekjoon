n = int(input())
arr = [[i]*2 for i in range(n, 0, -1)]

res = []
target = n
cnt = 0
while True:
    for i in range(n):
        for j in range(2):
            if arr[i][j] == target:
                start = (i,j)
                break
        else:
            continue
        break
    
    cnt += target-1-start[0]
    
    for i in range(start[0], target-1):
        res.append((i+1, target, min(arr[i+1])))
        arr[start[0]][start[1]] = min(arr[i+1])
        if (arr[i+1][0] < arr[i+1][1]): start = (i+1, 0)
        else: start = (i+1, 1)
        
    arr[start[0]][start[1]] = target
    
    if arr[target-1].count(target) == 2: target -= 1
    if target == 0:
        break

print(cnt)
for l in res:
    print(*l)