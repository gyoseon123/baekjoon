import sys
input = sys.stdin.readline

def p_list(n):
    p = [True]*(n+1)
    p[0],p[1] = False, False
    for i in range(2,int(n**0.5)+1):
        if p[i]:
            for j in range(i*2,n+1,i):
                p[j] = False
    return p

p = p_list(500000*2+1)

arr = [0]*500001
for i in range(2,500000+1):
    if p[i*2+1]:
        arr[i] = 1
for i in range(500000):
    arr[i+1] += arr[i]

q = int(input())
for _ in range(q):
    ans = 0
    x,y = map(int, input().split())
    print(arr[y-1] - arr[x-1])
    

