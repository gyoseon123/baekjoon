import sys
import random
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    s = input().rstrip()
    arr = set()
    for i in range(n-m+1):
        arr.add(s[i:i+m])
    
    while True:
        new_s = ''
        for i in range(m):
            new_s += chr(random.randint(1, k) + ord('a') - 1)
            
        if new_s not in arr:
            print(new_s)
            break
    

