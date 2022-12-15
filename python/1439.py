import sys
input = sys.stdin.readline
s = input().rstrip()

def check(target):
    temp = target
    cnt = 0
    for i in s:
        if i != temp:
            cnt += 1
            temp = i
    return cnt

print(min(check('1'), check('0')))

