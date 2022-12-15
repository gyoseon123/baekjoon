import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    d = {}
    n = int(input())
    for i in range(n):
        k,m = input().split()
        try:
            d[m] += 1
        except:
            d[m] = 1
    result = 1
    for i in d:
        result *= (d[i]+1)
    print(result-1)
        