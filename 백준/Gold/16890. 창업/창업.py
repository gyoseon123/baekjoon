saga = list(input())
cube = list(input())

saga.sort()
cube.sort(reverse = True)

sn = 0
cn = 0
snn = (len(saga)+1)//2 - 1
cnn = (len(cube))//2 - 1

left = 0
right = len(saga)-1

ans = ["?"]*len(saga)
turn = 1

while left <= right:
    # print(left, right, ans)
    if turn&1:
        if saga[sn] < cube[cn]:
            ans[left] = saga[sn]
            left += 1
            sn += 1
        else:
            ans[right] = saga[snn]
            right -= 1
            snn -= 1
    else:
        if saga[sn] >= cube[cn]:
            ans[right] = cube[cnn]
            right -= 1
            cnn -= 1
        else:
            ans[left] = cube[cn]
            left += 1
            cn += 1
    
    turn ^= 1

print("".join(ans))