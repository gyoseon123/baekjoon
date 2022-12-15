n = list(map(int, list(input())))
n.sort(reverse=True)
n = int(''.join(map(str, n)))
if n%30 == 0:
    print(n)
else:
    print(-1)