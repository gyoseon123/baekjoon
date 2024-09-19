from collections import deque
import sys
input = sys.stdin.readline

def cal(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i]:
            cnt += 1
        else:
            if cnt >= 4:
                for j in range(i-1, i-cnt-1, -1):
                    arr[j] = 0
                break
            cnt = 0
    else:
        if cnt >= 4:
            for j in range(i, i-cnt, -1):
                arr[j] = 0
    
    return arr

def check(arr):
    return arr.count(0) == len(arr)

def convert(arr):
    ret = 0
    cnt = 0
    for i in range(len(arr)):
        ret += arr[i]*(2**cnt)
        cnt += 1
    return ret

def bfs(start):
    q = deque()
    q.append((start, 0))
    res = []
    visited = [False]*(1 << n)

    while q:
        now, cnt = q.popleft()
        now = cal(now)

        if check(now):
            res.append(cnt)
            continue
        
        for i in range(n):
            if not now[i]:
                if i == 0 and i+1 < n and now[i+1]:
                    nn = now[:]
                    nn[i] = 1
                    if not visited[convert(nn)]:
                        visited[convert(nn)] = True
                        q.append((nn, cnt+1))
                elif i == n-1 and i-1 >= 0 and now[i-1]:
                    nn = now[:]
                    nn[i] = 1
                    if not visited[convert(nn)]:
                        visited[convert(nn)] = True
                        q.append((nn, cnt+1))
                else:
                    if i+1 < n and now[i+1]:
                        nn = now[:]
                        nn[i] = 1
                        if not visited[convert(nn)]:
                            visited[convert(nn)] = True
                            q.append((nn, cnt+1))
                    if i-1 >= 0 and now[i-1]:
                        nn = now[:]
                        nn[i] = 1
                        if not visited[convert(nn)]:
                            visited[convert(nn)] = True
                            q.append((nn, cnt+1))

    return res

n = int(input())
l = [int(input()) for _ in range(n)]

print(min(bfs(l)))