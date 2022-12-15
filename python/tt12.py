import sys
input = sys.stdin.readline
n = int(input())
num = [[0,i] for i in range(100001)]
for i in range(n):
    x = int(float(input())*1000)
    num[x][0] += 1
num.sort()
cnt = 0
def solve():
    global cnt
    for i in num:
        if i[0] != 0:
            for _ in range(i[0]):
                print(f'{i[1]/1000:.3f}')
                cnt += 1
                if cnt == 7:
                    return

solve()

    

# import sys
# input = sys.stdin.readline
# n = int(input())
# l = [float(input()) for _ in range(n)]
# l.sort()
# print(*l[:7], sep = '\n')