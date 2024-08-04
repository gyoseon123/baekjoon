t = int(input())
for _ in range(t):
    n,f,k = map(int, input().split())
    l = list(map(int, input().split()))
    fav = l[f-1]
    l.sort(reverse=True)
    fav_cnt = l.count(fav)

    for i in range(n):
        if l[i] == fav:
            first_fav = i
            break
    
    if first_fav+1 > k:
        print("NO")
    elif first_fav + fav_cnt <= k:
        print("YES")
    else:
        print("MAYBE")