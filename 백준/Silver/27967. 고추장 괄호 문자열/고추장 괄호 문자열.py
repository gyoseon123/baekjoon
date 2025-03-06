def check(l):
    stk = []
    for i in range(len(l)):
        if stk and l[i] == ")": stk.pop()
        else: stk.append(l[i])
    
    if not stk:
        print(''.join(l))
        exit()

def make(l, b):
    cnt = 0
    for i in range(len(l)):
        if l[i] == "G":
            if (b&(1<<cnt)): l[i] = ")"
            else: l[i] = "("
            cnt += 1
    check(l)

n = int(input())
s = list(input())

k = s.count("G")

for i in range(1<<k):
    make(s[:], i)