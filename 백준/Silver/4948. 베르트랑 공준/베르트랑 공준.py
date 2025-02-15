import sys

prime={} #소수 찾기

for i in range(2,500):
    prime[i]=0

prime2=prime.copy()

for i in prime2:
    for k in range(2,int(i**0.5)+1):
        if i%k==0:
            del prime[i]
            break
    
dict1={}
list1=[2]
for i in range(2, 250000):
    dict1[i] = 0
                    
for k in prime:
    list1.append(k)
    p=list1[-2]
    while k*p<=250000:
        if k*p in dict1:
            del dict1[k*p]
        p+=1

while True:
    n=int(sys.stdin.readline().strip())  
    if n==0:
         break
    else: #찐 소수 찾기
        cnt = 0
        for i in range(n+1,2*n+1):
            if i in dict1:
                cnt += 1
                
        print(cnt)