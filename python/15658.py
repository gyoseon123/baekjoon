import itertools
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
operator = ['+']*plus + ['-']*minus + ['*']*multiple + ['//']*divide
result = []

def calculation(arr):
    n = arr[0]
    for i in range(1,len(arr)//2+1):
        x = i*2-1
        if arr[x] == '+':
            n += arr[x+1]
        elif arr[x] == '-':
            n -= arr[x+1]
        elif arr[x] == '//':
            n //= arr[x+1]
        else:
            n *= arr[x+1]
    result.append(n)

for i in itertools.combinations(operator, n-1):
    s = []
    for j in range(2*n-1):
        if j&1 == 0:
            s.append(num[j//2])
        else:
            s.append(i[j//2])
    calculation(s)
print(max(result), min(result), sep='\n')
