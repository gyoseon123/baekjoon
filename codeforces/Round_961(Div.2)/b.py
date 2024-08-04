import random
import sys
input = sys.stdin.readline

RANDOM = random.randint(1, 10**10)
def hash(num):
    return num^RANDOM

def f(num1, cnt1, num2, cnt2):
    arr = [num1]*cnt1 + [num2]*cnt2
    ret = 0
    left = 0
    right = 0
    now = arr[0]
    while right < len(arr) and left <= right:
        if now > m:
            now -= arr[left]
            left += 1
        else:
            right += 1
            if right < len(arr):
                now += arr[right]
        if now <= m:
            ret = max(ret, now)
    return ret

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    sl = set()
    for i in l:
        sl.add(hash(i))
    cnt = {}
    for i in l:
        x = hash(i)
        try:
            cnt[x] += 1
        except:
            cnt[x] = 1
    ssl = sorted(list(sl))
    ans = 0
    for i in range(len(ssl)):
        if hash(hash(ssl[i])+1) in sl:
            ans = max(ans, f(hash(ssl[i]), cnt[ssl[i]], hash(ssl[i])+1, cnt[hash(hash(ssl[i])+1)]))
        else:
            ans = max(ans, f(hash(ssl[i]), cnt[ssl[i]], 0, 0))
    print(ans)

