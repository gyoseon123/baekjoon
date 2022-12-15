import sys
from collections import deque
input = sys.stdin.readline


def D(n):
    nx = n*2
    if nx > 9999:
        nx -= 10000
    return nx

def S(n):
    nx = n-1
    if n == 0:
        nx = 9999
    return nx

def L(n):
    nx = n//1000+10*(n%1000)
    return nx

def R(n):
    nx = 1000*(n%10)+n//10
    return nx


def solve(n):
    visited[n] = True
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == b:
            return
        m = D(x)
        if not visited[m]:
            visited[m] = True
            result[m] = (x,'D')
            q.append(m)
        m = S(x)
        if not visited[m]:
            visited[m] = True
            result[m] = (x,'S')
            q.append(m)
        m = L(x)
        if not visited[m]:
            visited[m] = True
            result[m] = (x,'L')
            q.append(m)
        m = R(x)
        if not visited[m]:
            visited[m] = True
            result[m] = (x,'R')
            q.append(m)

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    visited = [False]*10000
    result = [(0,'')]*10000
    solve(a)
    l = []
    while b != a:
        l.append(result[b][1])
        b = result[b][0]
    print(''.join(l[::-1]))