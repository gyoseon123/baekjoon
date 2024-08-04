import sys
input = sys.stdin.readline


def find(idx, target):
    for i in range(idx, len(a)):
        if a[i] == target:
            return i
        
    return -1

t = int(input())

for _ in range(t):
    a = input().rstrip()
    b = input().rstrip()

    ans = 0
    cnt = 0
    tmp = -1

    for start in range(len(b)):
        cnt = 0 
        tmp = -1
        for i in range(start,len(b)):
            f = find(tmp+1, b[i])
            if f != -1:
                cnt += 1
                tmp = f
                ans = max(ans, cnt)
            else:
                break

    print(len(a) + len(b) - ans)

        