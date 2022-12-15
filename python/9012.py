n = int(input())
for i in range(n):
    s = input()
    stk = []
    for j in s:
        stk.append(j)
        if len(stk) > 1:
            if stk[-1] == ')' and stk[-2] == '(':
                stk.pop()
                stk.pop()
    if len(stk) == 0:
        print('YES')
    else:
        print('NO')
        

