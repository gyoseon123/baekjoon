n,m = map(int, input().split())
l = list(map(int, input().split()))
l_sum = [0]
for i in range(n):
    l_sum.append(l_sum[i] + l[i])
for i in range(m):
    a,b = map(int, input().split())
    print(l_sum[b] - l_sum[a-1])

