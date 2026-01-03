import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [0] + list(map(int, input().split()))
psum = [0]*(n+1)
cnt = [0]*m
cnt[0] = 1

ans = 0
for i in range(1, n+1):
    psum[i] = (psum[i-1] + a[i])%m
    ans += cnt[psum[i]]
    cnt[psum[i]] += 1

print(ans)