import sys
input = sys.stdin.readline
k,n = map(int, input().split())
l = [int(input()) for _ in range(k)]
result = []

def check_len(n):
    cnt = 0
    for i in l:
        cnt += i//n
    return cnt


start = 0
end = sum(l)//k+1
while start <= end:
    mid = (start+end)//2
    if mid == 0:
        mid = 1
    c = check_len(mid)
    if c < n:
        end = mid-1
    else:
        start = mid+1
        result.append(mid)

print(max(result))

