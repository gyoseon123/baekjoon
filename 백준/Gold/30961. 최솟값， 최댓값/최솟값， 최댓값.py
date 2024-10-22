import sys
input = sys.stdin.readline

n = int(input())
l = sorted(list(set(list(map(int, input().split())))))

ans = l[-1]**2

for i in range(len(l)-1):
    ans ^= l[i]**2
    ans ^= l[i]*l[i+1]

print(ans)