import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coin = input().rstrip()
    t_locate = []
    for i in range(n):
        if coin[i] == "T":
            t_locate.append(i)
    
    if len(t_locate) == 0:
        print(0)
        continue
    
    if len(t_locate)%2 != 0:
        print(-1)
        continue
    
    cnt = 0
    stk = []
    for i in range(len(t_locate)):
        stk.append(t_locate[i])
        if len(stk) >= 2:
            fir = stk[-2]
            sec = stk[-1]
            if (sec - fir - 1)%2 == 0:
                cnt += (sec - fir - 1)//2 + (sec - fir + 1)//2
                stk.pop()
                stk.pop()
    
    if stk:
        print(-1)
    else:
        print(cnt)
