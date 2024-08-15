m = int(input())

dp = [[] for _ in range(10000)]

dp[1].append(1)
dp[2].append(3)
cnt = 0
for i in range(3, 10000):
    base = 1 + (1 << (i-1))
    dp[i].append(base)
    cnt += 1
    for j in range(i//2, 0, -1):
        for k in range(len(dp[i-j*2])):
            dp[i].append(base + (dp[i-j*2][k] << j))
            cnt += 1
        if cnt >= m:
            break
    else:
        continue
    break

cnt = 0
for i in range(1, 1000):
    for j in range(len(dp[i])):
        cnt += 1
        if cnt == m:
            print(dp[i][j])
            break
    else:
        continue
    break
