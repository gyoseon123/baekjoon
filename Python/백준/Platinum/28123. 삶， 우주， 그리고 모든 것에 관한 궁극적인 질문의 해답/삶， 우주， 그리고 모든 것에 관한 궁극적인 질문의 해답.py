n,k,x = map(int, input().split())
l = [0,1,2,2,3,3,3,3,4,4]

n -= l[x]
ans = n - 3*(k-1) + 1
if x in (4,8,9):
    ans += 1
print(ans)