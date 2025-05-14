import sys
import math
input = sys.stdin.readline
squared_1 = []
squared_2 = []
n = int(input())
for i in range(1,int(math.sqrt(50000))+1):
    squared_1.append(i**2)

def solve():
    if n in squared_1:
        print(1)
        return
    for i in range(len(squared_1)):
        for j in range(len(squared_1)):
            x = squared_1[i]+squared_1[j]
            if x == n:
                print(2)
                return
            if x < 50000:
                squared_2.append(x)
    for i in range(len(squared_1)):
        for j in range(len(squared_2)):
            if squared_1[i]+squared_2[j] == n:
                print(3)
                return
    print(4)

solve()