import sys
input = sys.stdin.readline
n = int(input())
n //= 3
def triangle(n):
    if n == 1:
        return ['  *  ', ' * * ', '*****']