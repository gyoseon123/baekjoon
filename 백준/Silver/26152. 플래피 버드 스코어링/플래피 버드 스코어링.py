import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
q = int(input())
w = list(map(int, input().split()))
c = []

for i in range(n):
    c.append(a[i] - b[i])

cc = [0]*n
cc[0] = c[0]
for i in range(1, n):
    cc[i] = min(cc[i-1], c[i])

for num in w:
    left = -1
    right = n
    
    while left + 1 < right:
        mid = (left + right)//2
        
        if cc[mid] < num:
            right = mid
        else:
            left = mid
        
    print(right)