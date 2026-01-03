import sys
input = sys.stdin.readline

def check(x):
    now = x
    flg = 1
    for i in range(n):
        now -= song[i][1]
        if now < 0: flg = 0
        now += song[i][0]
    return flg
    
n = int(input())
song = [list(map(int, input().split())) for _ in range(n)]

left = 0
right = int(1e9)

while left + 1 < right:
    mid = (left + right)//2
    if check(mid): right = mid
    else: left = mid

print(right)