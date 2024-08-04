import bisect
import sys
import random
input = sys.stdin.readline

RANDOM = random.randint(1, 10**10)
random_hash = lambda x : x^RANDOM


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(lambda x: random_hash(int(x)), input().split()))
    b = list(map(lambda x: random_hash(int(x)), input().split()))
    m = int(input())
    d = list(map(lambda x: random_hash(int(x)), input().split()))
    ori_d = d[:]
    d.sort()

    nums = {}
    same = set()
    for i in range(n):
        if a[i] != b[i]:
            try:
                nums[b[i]] += 1
            except:
                nums[b[i]] = 1
        else:
            same.add(a[i])
    
    try:
        if nums[ori_d[-1]] >= 1:
            flag = True
    except:
        flag = False

    if not flag and ori_d[-1] not in same:
        print("NO")
        continue


    for i,j in nums.items():
        if bisect.bisect_right(d, i) - bisect.bisect_left(d, i) < j:
            print("NO")
            break
    else:
        print("YES")

