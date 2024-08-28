import sys
input = sys.stdin.readline

def solve(cnt, now):
    global res
    
    if "".join(ans) > res:
        return
    
    if cnt+1 == n:
        res = min(res, "".join(ans))
        return
    
    flg = False
    if now < word[cnt+1]:
        flg = True
        solve(cnt+1, word[cnt+1])
        
    if now < r_word[cnt+1]:
        if flg:
            if r_word[cnt+1] > word[cnt+1]:
                return
        ans[cnt+1] = "1"
        solve(cnt+1, r_word[cnt+1])
        ans[cnt+1] = "0"

t = int(input())

for _ in range(t):
    n = int(input())
    word = [input().rstrip() for _ in range(n)]
    r_word = []
    for w in word:
        r_word.append(w[::-1])
    
    ans = ["0"]*n
    res = "1"*n
    
    solve(0, word[0])
    ans[0] = "1"
    solve(0, r_word[0])
    print(res)