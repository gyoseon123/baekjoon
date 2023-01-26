import sys
input = sys.stdin.readline
n,k = map(int, input().split())
ol = []
for i in range(n):
    l = list(map(int, input().split()))
    ol.append(l[1:4] + [l[0]])
ol.sort(reverse=True)

for i in range(n):
    if ol[i][3] == k:
        cnt = 0
        l = ol[i][0:3]
        for j in range(i-1,-1,-1):
            if ol[j][0:3] == l:
                cnt += 1
        print(i+1-cnt)
        break