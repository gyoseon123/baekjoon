import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = input().rstrip()
    b = input().rstrip()
    
    al = []
    acnt = [0]*3
    for i in range(len(a)):
        if a[i] != "B":
            al.append(a[i])
        
        if a[i] == "A": acnt[0] += 1
        elif a[i] == "B": acnt[1] += 1
        else: acnt[2] += 1
    
    bl = []
    bcnt = [0]*3
    for i in range(len(b)):
        if b[i] != "B":
            bl.append(b[i])
            
        if b[i] == "A": bcnt[0] += 1
        elif b[i] == "B": bcnt[1] += 1
        else: bcnt[2] += 1
    
    flg = 0
    for i in range(3):
        if abs(acnt[i] - bcnt[i])%2 != 0:
            flg = 1
    
    if flg:
        print("NO")
        continue
    
    astk = []
    bstk = []
    
    for s in al:
        if astk and astk[-1] == s:
            astk.pop()
        else:
            astk.append(s)
    
    for s in bl:
        if bstk and bstk[-1] == s:
            bstk.pop()
        else:
            bstk.append(s)
    
    print("YES" if astk == bstk else "NO")