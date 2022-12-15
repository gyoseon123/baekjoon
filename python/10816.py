import sys
import bisect

a = int(sys.stdin.readline())
a_list = sorted(list(map(int, sys.stdin.readline().split())))
b = int(sys.stdin.readline())
b_list = list(map(int, sys.stdin.readline().split()))
result = [0] * b
for i in range(b):
    result[i] = bisect.bisect_right(a_list,b_list[i]) - bisect.bisect_left(a_list,b_list[i])
for i in result:
    print(i)

