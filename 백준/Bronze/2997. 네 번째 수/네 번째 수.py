l = list(map(int, input().split()))

for i in range(-1000, 1000):
    ll = l[:] + [i]
    ll.sort()
    itv = ll[1] - ll[0]
    for j in range(3):
        if ll[j+1] - ll[j] != itv:
            break
    else:
        print(list(set(l)^set(ll))[0])
        break