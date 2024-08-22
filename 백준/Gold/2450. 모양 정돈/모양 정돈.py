import sys
input = sys.stdin.readline

def f(a,b,c):
    ret = 0
    cnt = 0
    
    for i in range(typ[a]):
        if l[i] != a:
            ret += 1
        if l[i] == b:
            cnt += 1
    
    for i in range(typ[a], typ[a] + typ[b]):
        if l[i] == c:
            ret += 1
        if l[i] == a:
            if cnt:
                cnt -= 1
            else:
                ret += 1
    
    return ret

        

n = int(input())
l = list(map(int, input().split()))
typ = [0,0,0,0]


for i in range(n):
    if l[i] == 1:
        typ[1] += 1
    if l[i] == 2:
        typ[2] += 1
    if l[i] == 3:
        typ[3] += 1

ans = min(f(1,2,3), f(1,3,2), f(2,1,3), f(2,3,1), f(3,1,2), f(3,2,1))
print(ans)