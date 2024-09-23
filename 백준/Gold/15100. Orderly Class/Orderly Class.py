import sys
input = sys.stdin.readline
INF = int(1e9)

a = input().rstrip()
b = input().rstrip()

left = 0
right = len(a)-1

for i in range(len(a)):
    if a[i] != b[i]:
        left = i
        break

for i in range(len(a)-1, -1, -1):
    if a[i] != b[i]:
        right = i
        break

ans = 0
if a[:left] + ''.join(reversed(list(a[left:right+1]))) + a[right+1:] == b:
    ans = 1
    while True:
        left -= 1
        right += 1
        
        if left < 0 or right >= len(a):
            break
        
        if a[left] == a[right]:
            ans += 1
        else:
            break
    
print(ans)