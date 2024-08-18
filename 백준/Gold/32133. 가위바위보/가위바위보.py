from collections import Counter
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
rsp = [input().rstrip() for _ in range(n)]

res = ""
for i in range(1, m+1):
    d = Counter([s[:i] for s in rsp])
    for key, val in d.items():
        if val <= k:
            res = key
            break
    else:
        continue
    break

if not res:
    print(-1)
else:
    print(len(res))
    for w in res:
        if w == "R":
            print("S", end='')
        elif w == "S":
            print("P", end='')
        else:
            print("R", end='')