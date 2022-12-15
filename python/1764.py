import sys
n,m = map(int, sys.stdin.readline().split())
hear = set()
look = set()
hear_and_look = []
for i in range(n):
    hear.add(sys.stdin.readline())
for i in range(m):
    look.add(sys.stdin.readline())
hear_and_look = sorted(list(hear&look))
print(len(hear_and_look))
for i in hear_and_look:
    print(i ,end = '')

