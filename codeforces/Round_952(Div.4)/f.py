def check(turn):
    damage = sum(att)
    turn -= 1
    for i in range(n):
        damage += att[i]*(turn//cool[i])
    
    if damage >= h:
        return True
    else:
        return False



t = int(input())


for _ in range(t):
    h,n = map(int, input().split())
    att = list(map(int, input().split()))
    cool = list(map(int, input().split()))
   
    left = 0
    right = int(1e11)

    while left + 1 < right:
        mid = (left + right)//2
        if check(mid):
            right = mid
        else:
            left = mid
    
    print(right)