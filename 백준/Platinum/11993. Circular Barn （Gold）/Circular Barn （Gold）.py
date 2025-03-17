import sys
input = sys.stdin.readline

def find_cow(target):
    zero_space.pop()
    dis = 1
    cow_pos = target-1
    if cow_pos == n:
        cow_pos = 0
    while (c[cow_pos] == 0):
        cow_pos -= 1 
        if cow_pos == -1:
            cow_pos = n-1
        dis += 1
    c[target] += 1
    c[cow_pos] -= 1
    d[target] = dis + d[cow_pos]
    if c[cow_pos] == 0:
        zero_space.append(cow_pos)
    return dis



n = int(input())
c = [int(input()) for _ in range(n)]
ans = 0
zero_space = []
d = [0]*n
for i in range(n):
    if c[i] == 0:
        zero_space.append(i)

while zero_space:
    find_cow(zero_space[-1])

print(sum([i**2 for i in d]))

