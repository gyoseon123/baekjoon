k = int(input())
dp = [0]*(k+1)
for i in range(k, -1, -1):
    for j in range(1,int(i**0.5)+1):
        if i%j == 0:
            if i+j <= k and not dp[i+j]:
                dp[i] = 1
                break
            if i+i//j <= k and not dp[i+i//j]:
                dp[i] = 1
                break
if dp[1] == 1:
    print('Kali')
else:
    print('Ringo')