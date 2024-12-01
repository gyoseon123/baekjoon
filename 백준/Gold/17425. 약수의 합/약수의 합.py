import sys
input = sys.stdin.readline

div = [0]*1000001

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        div[j] += i

for i in range(1000000):
    div[i+1] += div[i]
    
t = int(input())

for _ in range(t):
    print(div[int(input())])