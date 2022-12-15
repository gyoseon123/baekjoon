num = int(input())
x = 2
result = []
while num != 1:
    if num % x == 0:
        num /= x
        result.append(x)
    else:
        x += 1
for i in result:
    print(i)