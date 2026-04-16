import sys
input = sys.stdin.readline

def rot(arr):
    return list(map(list, zip(*arr)))[::-1]

def fill_55(x,y, rev):
    for i in range(5):
        for j in range(5):
            if rev: ans[x+i][y+j] = block55[i][j]
            else: ans[x+i][y+j] = block55_rev[i][j]
            
def fill_35(x,y, rev):
    for i in range(5):
        for j in range(3):
            if rev: ans[x+i][y+j] = block35[i][j]
            else: ans[x+i][y+j] = block35_rev[i][j]
            
def fill_45(x,y, rev):
    for i in range(5):
        for j in range(4):
            if rev: ans[x+i][y+j] = block45[i][j]
            else: ans[x+i][y+j] = block45_rev[i][j]

def fill_210(x, y):
    for i in range(10):
        for j in range(2):
            ans[x+i][y+j] = block210[i][j]
            
def fill_215(x, y):
    for i in range(15):
        for j in range(2):
            ans[x+i][y+j] = block215[i][j]
    
block210 = [["L", "L"], 
           ["I", "L"], 
           ["I", "L"], 
           ["I", "L"],
           ["I", "N"], 
           ["I", "N"],
           ["N", "N"],
           ["N", "P"],
           ["P", "P"],
           ["P", "P"]]

block215 = [["L", "L"], 
           ["I", "L"], 
           ["I", "L"], 
           ["I", "L"],
           ["I", "N"], 
           ["I", "N"],
           ["N", "N"],
           ["N", "Y"],
           ["Y", "Y"],
           ["I", "Y"],
           ["I", "Y"],
           ["I", "L"],
           ["I", "L"],
           ["I", "L"],
           ["L", "L"]]

block35 = [["Y", "L", "L"],
           ["Y", "Y", "L"], 
           ["Y", "T", "L"], 
           ["Y", "T", "L"], 
           ["T", "T", "T"]]


block45 = [["V", "V", "V", "I"], 
           ["V", "N", "L", "I"], 
           ["V", "N", "L", "I"], 
           ["N", "N", "L", "I"], 
           ["N", "L", "L", "I"]]

block55 = [["I", "I", "I", "I", "I"],
           ["Y", "U", "U", "L", "L"], 
           ["Y", "Y", "U", "V", "L"],
           ["Y", "U", "U", "V", "L"],
           ["Y", "V", "V", "V", "L"]]

block35_rev = [["N", "L", "L"],
               ["N", "N", "L"],
               ["V", "N", "L"],
               ["V", "N", "L"],
               ["V", "V", "V"]]

block45_rev = [["I", "U", "U", "U"],
               ["I", "U", "N", "U"],
               ["I", "P", "N", "N"], 
               ["I", "P", "P", "N"], 
               ["I", "P", "P", "N"]]

block55_rev = [["P", "P", "P", "L", "L"], 
               ["P", "P", "Z", "Z", "L"],
               ["U", "U", "Z", "T", "L"],
               ["U", "Z", "Z", "T", "L"],
               ["U", "U", "T", "T", "T"]]


h,w = map(int, input().split())
ans = [[""]*w for _ in range(h)]

if h == 1 and w == 5:
    print("yes")
    print("IIIII")
    exit()
    
if h == 5 and w == 1:
    print("yes")
    print(*["I"]*5, sep='\n')
    exit()

if h == 2 and w%10 == 0:
    ans = rot(ans)
    
    h,w = w,h
    
    for i in range(0, h, 10):
        for j in range(0, w, 2):
            fill_210(i, j)
            
    ans = rot(rot(rot(ans)))
    
    h,w = w,h
    
    print("yes")
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end='')
        print()
        
    exit()

if h%10 == 0 and w == 2:
    
    for i in range(0, h, 10):
        for j in range(0, w, 2):
            fill_210(i, j)
    
    print("yes")
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end='')
        print()
        
    exit()

if h == 2 and w%5 == 0 and w != 5:
    block210.reverse()
        
    ans = rot(ans)
    h,w = w,h
    
    fill_215(0, 0)
    
    for i in range(15, h, 10):
        for j in range(0, w, 2):
            fill_210(i, j)
            
    ans = rot(rot(rot(ans)))
    
    h,w = w,h
    
    print("yes")
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end='')
        print()
        
    exit()

if h%5 == 0 and h != 5 and w == 2:
    block210.reverse()
    
    fill_215(0, 0)
    
    for i in range(15, h, 10):
        for j in range(0, w, 2):
            fill_210(i, j)
    
    print("yes")
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end='')
        print()
        
    exit()
    

if h%5 == 0 and w%5 == 0:
    rev = 0
    for j in range(0, w, 5):
        rev ^= 1
        for i in range(0, h, 5):
            fill_55(i, j, rev)
            
    print("yes")
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end='')
        print()
        
    exit()

if (h*w)%5 != 0 or w == 1 or h == 1 or w == 2 or h == 2:
    print("no")
    exit()



    
flg = 0
if w%5 == 0:
    h,w = w,h
    flg = 1
    ans = rot(ans)

cnt = 0
ww = w
while ww%3 != 0:
    ww -= 4
    cnt += 1

ocnt = cnt

for j in range(0, w, 4):
    rev = 0
    if cnt == 0: break
    cnt -= 1
    for i in range(0, h, 5):
        rev ^= 1
        fill_45(i, j, rev)

rev = ocnt&1
for j in range(ocnt*4, w, 3):
    rev ^= 1
    for i in range(0, h, 5):
        fill_35(i, j, rev)

if flg:
    ans = rot(rot(rot(ans)))
    h,w = w,h
    
print("yes")
for i in range(h):
    for j in range(w):
        print(ans[i][j], end='')
    print()