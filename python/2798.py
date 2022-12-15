a,b = map(int, input().split())
array = list(map(int, input().split()))
num = []
for i in range(a):
    for j in range(1, a):
        for o in range(2, a):
            if i != j and j != o and o != i:
                num.append(array[i]+array[j]+array[o])
num = [i for i in num if i <= b]
print(max(num))
