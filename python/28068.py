import sys
input = sys.stdin.readline
n = int(input())
plus = []
minus = []

for _ in range(n):
    a,b = map(int, input().split())
    if a <= b:
        plus.append((a,b))
    else:
        minus.append((a,b))
        
plus.sort()
minus.sort(key = lambda x : x[1],reverse = True)

now = 0
for a,b in plus:
    if a <= now:
        now += b-a
    else:
        print(0)
        exit()

for a,b in minus:
    if a <= now:
        now -= (a-b)
    else:
        print(0)
        break
else:
    print(1)
