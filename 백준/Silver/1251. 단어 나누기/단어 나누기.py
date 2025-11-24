a=input()
l=len(a)
t="z"*100
for i in range(1,l-1):
    for j in range(i+1,l):
        if a[:i][::-1]+a[i:j][::-1]+a[j:][::-1]<t:
            t=a[:i][::-1]+a[i:j][::-1]+a[j:][::-1]
print(t)