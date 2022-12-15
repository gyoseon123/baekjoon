import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()
i = 0
cnt = 0
check = 0
while i < m-1:
    if s[i:i+3] == 'IOI':
        i += 2
        check += 1
        if check == n:
            cnt += 1
            check -= 1    
    else:
        i += 1
        check = 0
print(int(cnt))

