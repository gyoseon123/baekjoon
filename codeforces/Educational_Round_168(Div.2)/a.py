import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().rstrip()
    cnt = 0
    ans = ""
    flag = False
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            for w in ('a', 'b', 'c'):
                if w != s[i] and w != s[i-1]:
                    ans = s[:i] + w + s[i:]
                    flag = True
                    break
        if flag:
            break
    if not ans:
        for w in ('a', 'b'):
            if w != s[-1]:
                ans = s + w
    
    print(ans)
           
