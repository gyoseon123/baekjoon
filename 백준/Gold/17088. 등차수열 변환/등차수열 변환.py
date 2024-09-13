import sys
input = sys.stdin.readline
INF = sys.maxsize

def find_seq(a, d):
    ret = [a]
    for i in range(1,n):
        ret.append(a + d*i)
    return ret

def cal(arr):
    cnt = 0
    for i in range(n):
        if abs(arr[i] - l[i]) <= 1:
            cnt += abs(arr[i] - l[i])
        else:
            return INF
    return cnt
    
n = int(input())
l = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()
    
ans = INF

for i in range(-1, 2):
    for j in range(-1,2):
        ans = min(ans, cal(find_seq(l[0]+i, l[1]+j - (l[0]+i))))

print(ans if ans != INF else -1)
