import collections
def find_mode():
    mx = max(check)
    x = 0
    for i,num in enumerate(check):
        if num == mx:
            x += 1
            result = i
        if x == 2:
            break
    return result - 4000


n = int(input())
nums = []
check = [0]*8001
for i in range(n):
    nums.append(int(input()))
    check[nums[-1]+4000] += 1
nums.sort()
print(round(sum(nums)/n))
print(nums[len(nums)//2])
x = sorted(collections.Counter(nums).most_common(), key = lambda x : x[0])
if len(x) == 1:
    print(x[0][1])
else:
    if x[0][1] == x[1][1]:
        print(x[1][0])
    else:
        print(x[0][0])
print(nums[-1] - nums[0])

