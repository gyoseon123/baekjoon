import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
ans = False

fir = 0 
sec = 0

for i in range(0, n*3, 3):
    fir += l[i]
    sec += l[i+1]

if fir != sec:
    ans = True

l.sort()

fir = 0
sec = 0

for i in range(0, n*3, 3):
    fir += l[i]
    sec += l[i+1]

if fir != sec:
    ans = True

print("Y" if ans else "N")