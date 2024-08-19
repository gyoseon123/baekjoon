p = pow
def s(n):
    if n==1:return 1
    elif n%2==0:return(s(n//2)*(1+p(a,n//2,m)))%m
    else:return(s(n-1)+p(a,n-1,m))%m
m,a,c,X,n,g=map(int,input().split())
print((X*p(a,n,m)+c*s(n))%m%g)