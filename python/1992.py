import sys
input = sys.stdin.readline
n = int(input())
image = [list(map(int, list(input().rstrip()))) for _ in range(n)]
result = ''
def quadtree(n,arr):
    global result
    size = n*n
    cnt = sum([i.count(1) for i in arr])
    if cnt == size:
        result += '1'
    elif cnt == 0:
        result += '0'
    else:
        result += '('
        quadtree(n//2,[i[0:n//2] for i in arr[0:n//2]])
        quadtree(n//2,[i[n//2:n] for i in arr[0:n//2]])
        quadtree(n//2,[i[0:n//2] for i in arr[n//2:n]])
        quadtree(n//2,[i[n//2:n] for i in arr[n//2:n]])
        result += ')'
quadtree(n,image)
print(result)