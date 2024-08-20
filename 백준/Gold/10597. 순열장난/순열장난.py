def solve(cnt, now):
    if now != s[:len(now)] or len(now) > len(s):
        return
    
    if now == s and set(trac[:cnt]) == set([i for i in range(1, cnt+1)]):
        print(*trac[:cnt])
        exit()

    for i in range(1, 51):
        if i in trac[:cnt]:
            continue

        trac[cnt] = i
        solve(cnt+1, now + str(i))

trac = [0]*50
s = input()
solve(0, '')