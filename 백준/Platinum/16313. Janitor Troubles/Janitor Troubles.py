from math import sqrt
import sys
input = sys.stdin.readline

a,b,c,d = map(int, input().split())
s = (a + b + c + d)/2

print(sqrt((s - a) * (s - b) * (s - c) * (s - d)))