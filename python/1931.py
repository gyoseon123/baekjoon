import sys
input = sys.stdin.readline
n = int(input())
time = []
for i in range(n):
    a,b = map(int, input().split())
    time.append((a,b))
time.sort(key = lambda x : (x[0],abs(x[0]-x[1])))
print(time)