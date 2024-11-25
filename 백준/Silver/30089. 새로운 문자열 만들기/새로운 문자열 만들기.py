import sys
input = sys.stdin.readline

def is_pal(s):
    return s == s[::-1]

t = int(input())

for _ in range(t):
    s = input().rstrip()
    maxx = 0 
    for i in range(len(s)):
        if is_pal(s[i:]):
            maxx = max(maxx, len(s)-i)
    
    print(s + s[:len(s)-maxx][::-1])