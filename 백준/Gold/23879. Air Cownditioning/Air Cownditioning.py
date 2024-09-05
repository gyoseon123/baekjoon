import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

for i in range(n):
    c.append(a[i] - b[i])

l = [c[0]]
for i in range(n-1):
    l.append(c[i+1] - c[i])

print(max(sum([num for num in l if num > 0]), -sum([num for num in l if num < 0])))