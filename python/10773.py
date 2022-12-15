n = int(input())
stk = []
for i in range(n):
    a = int(input())
    if a == 0:
        stk.pop()
    else:
        stk.append(a)
print(sum(stk))