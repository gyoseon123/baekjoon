import sys
input = sys.stdin.readline
n,m = map(int, input().split())
student = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    student[x].append(y)
