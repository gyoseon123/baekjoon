import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if (a == b): return
    
    if rank[a] < rank[b]: a,b = b,a
    parent[b] = a
    if (rank[a] == rank[b]): rank[a] += 1

n = int(input())
p, *left = list(map(int, input().split()))
q, *right = list(map(int, input().split()))
parent = [i for i in range(n)]
rank = [0]*(n)

graph = [[1]*n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
    
if p + q >= n*(n-1)//2+1:
    if n != 2 and n%2 == 0: flg = 0
    
    if p + q > n*(n-1)//2 + 1:
        print("N")
        exit()
    
    arr = left[:]
    x = n*(n-1)//2+1 - p
    a = []
    flg = 1
    
    rem = p + q - n*(n-1)//2 - 1
    
    for i in range(rem):
        if right[i] != left[p-rem+i]: flg = 0
    
    if not flg:
        print("N")
        exit()
    
    for i in range(q-1, q-1-x, -1):
        a.append(right[i])
    
    arr.extend(a[::-1])
    
    for i in range(len(arr)-1):
        if graph[arr[i+1]-1][arr[i]-1] == 0: flg = 0
        if graph[arr[i]-1][arr[i+1]-1] == 0: flg = 0
        if arr[i] == arr[i+1]: flg = 0
        
        graph[arr[i+1]-1][arr[i]-1] = 0
        graph[arr[i]-1][arr[i+1]-1] = 0
        
    print("Y" if sum(map(sum, graph)) == 0 and flg else "N")
else:
    flg = 1
    for i in range(p-1):
        if graph[left[i]-1][left[i+1]-1] == 0: flg = 0
        if graph[left[i+1]-1][left[i]-1] == 0: flg = 0
        if left[i] == left[i+1]: flg = 0
        
        graph[left[i]-1][left[i+1]-1] = 0
        graph[left[i+1]-1][left[i]-1] = 0
    
    for i in range(q-1):
        if graph[right[i]-1][right[i+1]-1] == 0: flg = 0
        if graph[right[i+1]-1][right[i]-1] == 0: flg = 0
        if right[i] == right[i+1]: flg = 0
        
        graph[right[i]-1][right[i+1]-1] = 0
        graph[right[i+1]-1][right[i]-1] = 0
    
    degree = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j]:
                degree[i] += 1
                degree[j] += 1
                union(i,j)
    
    s = set([find(i) for i in range(n) if degree[i] != 0])
    
    if (len(s) != 1):
        flg = 0
    
    odd = 0
    even = 0
    for i in range(n):
        if degree[i]%2 == 0: even += 1
        else: odd += 1
    
    if not (odd == 2 or odd == 0):
        flg = 0
    
    if (p == 0 and q != 0):
        if degree[right[0]-1]%2 == 0:
            if odd == 2 or degree[right[0]-1] == 0: flg = 0
    elif (p != 0 and q == 0):
        if degree[left[-1]-1]%2 == 0:
            if odd == 2 or degree[left[-1]-1] == 0: flg = 0
    elif (p != 0 and q != 0):
        if degree[left[-1]-1] == 0: flg = 0
        if degree[right[0]-1] == 0: flg = 0
        
        if (left[-1] == right[0]):
            if odd == 2: flg = 0
        else:
            if degree[left[-1]-1]%2 == 0: flg = 0
            if degree[right[0]-1]%2 == 0: flg = 0
    else:
        if n != 2 and n%2 == 0: flg = 0
    
    print("Y" if flg else "N")