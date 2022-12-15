import math
def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i == 0:
            return 0
    return 1
while True:
    count = 0
    num = int(input())
    if num == 0:
        break
    for i in range(num+1, num*2+1):
        count += prime(i)
    print(count)