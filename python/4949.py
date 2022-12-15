while True:
    s = input()
    if s == '.':
        break
    new_s = ''
    stk = []
    for i in s:
        if i == '(' or i == ')' or i == '[' or i == ']':
            new_s += i
    for i in new_s:
        stk.append(i)
        if len(stk) > 1:
            if (stk[-1] == ')' and stk[-2] == '(') or (stk[-1] == ']' and stk[-2] == '['):
                stk.pop()
                stk.pop()
    if len(stk) == 0:
        print('yes')
    else:
        print('no')