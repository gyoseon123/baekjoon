import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
if m != 0:
    l = list(map(int, input().split()))
else:
    l = [-1]
def check(n):
    if n == 0 and n not in button:
        return False
    while n > 0:
        x = n%10
        if x not in button:
            return False
        n //= 10
    return True
if m == 0:
    button = [i for i in range(10)]
else:
    button = [i for i in range(10) if i not in l]
    button.reverse()
result = []
b = []
for i in range(0,1000001):
    if check(i):
        result.append(abs(n-i))
        b.append(i)
length = []
if not result:
    m = 0
else:
    m = min(result)
for i in range(len(result)):
    if result[i] == m:
        length.append(len(str(b[i])))
if not result:
    print(abs(100-n))
else:
    if abs(100-n) <= m + min(length):
        print(abs(100-n))
    else:
        print(m + min(length))
