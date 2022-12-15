import sys
input = sys.stdin.readline
n,r,c = map(int, input().split()) 
result = 0
def z(n,x,y):
    global result
    if n == 0:
        return
    half = 2**(n-1)
    nx,ny = x//half, y//half
    if (nx,ny) == (0,0):  #2사분면
        z(n-1,x%half, y%half)
    elif (nx,ny) == (0,1):  #1사분면
        result += half*half
        z(n-1,x%half, y%half)
    elif (nx,ny) == (1,0):  #3사분면
        result += half*half*2
        z(n-1,x%half, y%half)
    else:  #4사분면
        result += half*half*3
        z(n-1,x%half, y%half)
z(n,r,c)
print(result)


    
