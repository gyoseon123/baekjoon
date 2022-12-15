import sys
input = sys.stdin.readline
a,b,c = map(int, input().split())
def multiple(x,y):
    print(x,y)
    if y == 1:
        return x%c
    t = multiple(x,y//2)
    if y%2 == 1:
        return (t*t*x)%c
    else:
        return (t*t)%c
print(multiple(a,b))