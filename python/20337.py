import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append((l[i], i+1))

arr.sort()

fir = set()
sec = set()
thr = [i for i in range(n//2+1, n+1)]

for i in range(n//4):
    fir.add(arr[i][1])

cnt = 0
for i in range(1,n//4+1):
    if i in fir:
        cnt += 1
    else:
        fir.add(i)

i = 1
while cnt:
    if i not in fir:
        fir.add(i)
        cnt -= 1
    else:
        i += 1

fv = {} 
fl = list(fir)
for i in range(n//2):
    fv[l[fl[i]-1]] = fl[i]


for i in range(n//4, n//2):
    sec_val = arr[i][1]
    if sec_val in fir:
        print(sec_val)
        sec.add(fv[sec_val])
    else:
        sec.add(sec_val)

for i in range(n//4+1,n//2+1):
    if i in sec:
        cnt += 1
    else:
        sec.add(i)

i = 1
while cnt:
    if i not in sec:
        sec.add(i)
        cnt -= 1
    else:
        i += 1

print(3)

print(*list(fir))
print(*list(sec))
print(*thr)

