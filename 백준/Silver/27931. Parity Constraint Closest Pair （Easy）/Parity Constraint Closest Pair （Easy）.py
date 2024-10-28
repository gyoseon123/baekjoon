import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
l = list(map(int, input().split()))
l.sort()
odd = []
even = []

for i in range(n):
    if l[i]&1:
        odd.append(l[i])
    else:
        even.append(l[i])

even_ans = INF

for i in range(len(odd)-1):
    even_ans = min(even_ans, odd[i+1] - odd[i])

for i in range(len(even)-1):
    even_ans = min(even_ans, even[i+1] - even[i])

odd_ans = INF

for i in range(n-1):
    if (l[i+1] - l[i])&1:
        odd_ans = min(odd_ans, l[i+1] - l[i])

even_ans = -1 if even_ans == INF else even_ans
odd_ans = -1 if odd_ans == INF else odd_ans

print(even_ans, odd_ans)