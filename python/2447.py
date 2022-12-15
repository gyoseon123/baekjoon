import sys
input = sys.stdin.readline

def asterisk(n):
    if n == 1:       #조건
        return ['*']
    star = asterisk(n//3)   #분할
    result = []
    for i in star:   #조합
        result.append(i*3)
    for i in star:
        result.append(i + ' '*(n//3) + i)
    for i in star:
        result.append(i*3)
    return result
print(*asterisk(int(input())), sep='\n')