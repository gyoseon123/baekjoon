import sys
input = sys.stdin.readline

def gcd(a,b):
    if b != 0:
        return (gcd(b, a%b))
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

n = int(input())
l = [0] + list(map(int, input().split()))

cycle = []
visited = [False]*(n+1)

for i in range(1, n+1):
    if not visited[l[i]]:
        visited[l[i]] = True
        cnt = 1
        now = l[i]
        while True:
            next = l[now]
            if visited[next]:
                break
            else:
                visited[next] = True
                now = next
                cnt += 1
        cycle.append(cnt)

ans = 1
for i in range(len(cycle)):
    ans = lcm(ans, cycle[i])

print(ans)