import sys
input = sys.stdin.readline

a,b = map(int, input().split())

ans = 0

while True:
    for i in range(64):
        x = ans + (1 << i)
        if a <= x and x <= b:
            ans += (1 << i)
            print(ans)
            exit()
        elif b < x:
            ans += (1 << (i-1))
            break