import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a,b = input().split()
    print("Distances: ", end="")
    for i in range(len(a)):
        val = ord(b[i]) - ord(a[i])
        if val < 0:
            val += 26
        print(val, end=' ')
    print()
        