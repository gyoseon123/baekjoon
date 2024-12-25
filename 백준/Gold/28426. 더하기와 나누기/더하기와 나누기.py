n = int(input())
if n == 2:
    print(2,4)
    exit()
sum_ = 0
for i in range(2,2*n,2):
    print(i, end=' ')
    sum_ += i
for i in range(3,1000000+1,2):
    if (sum_+i)%i == 0:
        print(i)
        break