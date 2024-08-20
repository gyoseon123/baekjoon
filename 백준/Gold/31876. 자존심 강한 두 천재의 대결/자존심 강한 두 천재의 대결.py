import sys
input = sys.stdin.readline

u,v = map(int, input().split())

a = input().rstrip()
b = input().rstrip()

if len(a) >= 22:
    if u > v:
        print("ras")
    elif u < v:
        print("auq")
    else:
        if a == b:
            print("rasauq")
        elif a < b:
            print("auq")
        else:
            print("ras")
else:
    a = int(a, u)
    b = int(b, v)
    if a == b:
        print("rasauq")
    elif a < b:
        print("auq")
    else:
        print("ras")
