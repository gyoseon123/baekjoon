import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

arr1 = [0]*n #i-1번째에 2를 몇번 곱해야 i번째보다 커지는가
arr2 = [0]*n #i번째에 2를 몇번 곱해야 i-1번째보다 커지는가

for i in range(1, n):
    cnt = 0
    now = l[i]
    while l[i-1] > now*2**cnt:
        cnt += 1
    arr1[i] = cnt

    cnt = 0
    now = l[i]
    while now > l[i-1]:
        now //= 2
        cnt += 1
    arr2[i] = cnt

print(arr1)
print(arr2)

ans = 0
m = 0
for i in range(1, n):
    if arr1[i-1] - arr2[i] > 0:
        m += arr1[i-1] - arr2[i]
        arr1[i] = arr1[i-1] - arr2[i]
    ans += arr1[i] + m

print(arr1)
print(ans)





