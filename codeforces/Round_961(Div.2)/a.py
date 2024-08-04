import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    for i in range(1, n):
        arr.append(i)
    
    arr.sort(reverse=True)
    cnt = 0
    for i in range(len(arr)):
        if k >= arr[i]:
            k -= arr[i]
            cnt += 1
        else:
            if k != 0:
                cnt += 1
            break
    print(cnt)

        
