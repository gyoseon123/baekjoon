n = int(input())
stk = []
for i in range(n):
    a = input()
    if a.startswith("push"):
        stk.append(int(a.split()[1]))
    if a == 'top':
        print(stk[-1])
    if a == 'size':
        print(len(stk))
    if a == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    if a == 'pop':
        if len(stk) != 0:
            print(stk.pop())
        else:
            print(-1)
    
