a = int(input())
num = []
for i in range(1,1000001):
    x = i + sum(map(int, (list(str(i)))))
    if x == a:
        num.append(i)
if len(num) == 0:
    print(0)
else:
    print(min(num))