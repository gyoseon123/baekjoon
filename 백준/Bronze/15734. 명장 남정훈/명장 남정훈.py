l,r,a = map(int, input().split())

ans = 0

for i in range(a+1):
    ans = max(ans, min(l+i, r+a-i)*2)

print(ans)