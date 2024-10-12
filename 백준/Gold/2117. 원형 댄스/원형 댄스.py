n = int(input())

x = n//2-1
if n%2 == 0:
    print(x*(x+1))
else:
    print(x*(x+1)//2 + (x+2)*(x+1)//2)