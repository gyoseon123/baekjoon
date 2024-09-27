from functools import cmp_to_key
import sys
input = sys.stdin.readline

def cmp(a,b):
    if int(a + b) < int(b + a):
        return 1
    else:
        return -1

n = int(input())
l = list(input().split())

l.sort(key=cmp_to_key(cmp))
print(int("".join(l)))