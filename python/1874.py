n = int(input())
stk = []
array = []
result = []
for i in range(n):
    stk.append(int(input()))
for i in range(1,n+1):
    array.append(i)
    result.append('+')
    while array[-1] == stk[0]:
        array.pop()
        stk.pop(0)
        result.append('-')
        if len(array) == 0:
            break
if len(array) == 0:
    for i in result:
        print(i)
else:
    print('NO')
