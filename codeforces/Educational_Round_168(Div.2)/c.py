import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().rstrip())
    s[0] = "("

    val = 0
    for i in range(n):
        if s[i] == "(":
            val += 1
        elif s[i] == ")":
            val -= 1
        else:
            if val > 0:
                s[i] = ")"
                val -= 1
            else:
                s[i] = "("
                val += 1
    

    stk = []
    ans = 0
    for i in range(n):
        if stk and stk[-1] == "(" and s[i] == ")":
            stk.pop()
            ans += 1 + len(stk)*2
        else:
            stk.append(s[i])
    
    print(ans)
        

    
