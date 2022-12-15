t = int(input())

def solve(n):
    if len(s) == 10:
        return True
    l = list(str(n))
    for i in l:
        if i not in s:
            s.add(i)

for i in range(t):
    s = set()
    n = int(input())
    if n == 0:
        print(f'Case #{i+1}: INSOMNIA')
        continue
    x = 1
    while True:
        if solve(n*x):
            print(f'Case #{i+1}: {n*(x-1)}')
            break
        x += 1
    
    