import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

while s != s.replace("PS4", "PS") or s != s.replace("PS5", "PS"):
    s = s.replace("PS4", "PS")
    s = s.replace("PS5", "PS")

print(s)