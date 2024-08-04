import random
import sys
input = sys.stdin.readline
RANDOM = random.randint(1, 10**10)

def wrap(num):
    return num^RANDOM


t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    mod = dict()

    if n == 1:
        print(0)
        continue

    for i in range(n):
        m = a[i]%k
        try:
            mod[wrap(m)].append(a[i])
        except:
            mod[wrap(m)] = [a[i]]
    
    ans = 0
    cnt = 0
    for i,l in mod.items():
        if len(l)%2 != 0:
            cnt += 1
            l.sort()

            max_itv = -1
            max_itv_idx = 0
            for i in range(len(l)-1):
                if l[i+1] - l[i] > max_itv:
                    max_itv = l[i+1] - l[i]
                    max_itv_idx = i
            
            l1 = []
            l2 = []
            for i in range(len(l)):
                if i != max_itv_idx:
                    l1.append(l[i])
                if i != max_itv_idx+1:
                    l2.append(l[i])

            ret1 = 0
            ret2 = 0
            for i in range(0,len(l1), 2):
                ret1 += (l1[i+1] - l1[i])//k
                ret2 += (l2[i+1] - l2[i])//k
            
            print(l1, l2)
            
            print(ret1, ret2)
            ans += min(ret1, ret2)
            

            if cnt == 2:
                print(-1)
                exit()
            continue
        
        l.sort()
        for i in range(0,len(l), 2):
            ans += (l[i+1] - l[i])//k
    
    print(ans)
        


