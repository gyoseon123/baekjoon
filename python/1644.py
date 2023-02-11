import math
n = int(input())

def prime_list(x):
    p = [True] * x
    for i in range(2,int(math.sqrt(x))+1):
        if p[i] == True:
            for j in range(i+i,x,i):
                p[j] = False
    return [i for i in range(2,x) if p[i] == True]

p = prime_list(8000000)
left = 0
right = 0
now = p[0]
cnt = 0
while p[left] <= n and left <= right:
    if now == n:
        cnt += 1
        left += 1
        right += 1
        now = sum(p[left:right+1])
    elif now < n:
        right += 1
        now += p[right]
    else:
        now -= p[left]
        left += 1

print(cnt)
        
    