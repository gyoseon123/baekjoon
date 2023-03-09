import sys
input = sys.stdin.readline
def prime_list(n):
    p = [True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if p:
            for j in range(i*2, n, i):
                p[j] = False
    return [i for i in range(2,n+1) if p[i]]
n = int(input())
p = prime_list(n)
left = 0
right = len(p)-1
while left <= right:
    mid = (left+right)//2
    print(f"? {p[mid]}")
    sys.stdout.flush()
    ans = int(input())
    if ans == 0:
        right = mid-1
    else:
        left = mid+1
print(f"! {p[(mid+left)//2]}")