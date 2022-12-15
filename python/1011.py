def a(n):
    return n*(n+1)/2
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    dis = y-x
    count = 0
    while count != dis:
        n = 1
        count += n
        
        n += 1