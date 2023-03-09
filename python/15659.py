import sys
input = sys.stdin.readline
max_num = -sys.maxsize
min_num = sys.maxsize

def cal(order, index, a, b, c, d):
    global max_num, min_num
    
    if index == n:
        s = str(nums[0])
        for i in range(n-1):
            now = order[i]
            if now == 1:
                s += '+'
            elif now == 2:
                s += '-'
            elif now == 3:
                s += '*'
            else:
                s += '//'
            s += str(nums[i+1])
        max_num = max(max_num, eval(s))
        min_num = min(min_num, eval(s))
        return
    if a >= 1:
        cal(order + [1], index + 1, a - 1, b, c, d)
    if b >= 1:
        cal(order + [2], index + 1, a, b - 1, c, d)
    if c >= 1:
        cal(order + [3], index + 1, a, b, c - 1, d)
    if d >= 1:
        cal(order + [4], index + 1, a, b, c, d - 1)



n = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
cal([], 1, a, b, c, d)
print(max_num)
print(min_num)