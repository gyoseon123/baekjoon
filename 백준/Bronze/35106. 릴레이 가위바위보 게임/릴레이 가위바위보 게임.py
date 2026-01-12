import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = [0]*3

for num in a:
    cnt[num-1] += 1

b = []
for i in range(3):
    b.append((cnt[i], i))

b.sort()

print(b[0][1]+1, b[2][1]+1, sep='\n')