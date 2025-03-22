import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

cnt = [0]*12

for i in range(len(a)):
    if a[i] + b[i] == "AC":
        cnt[0] += 1
    if a[i] + b[i] == "CA":
        cnt[1] += 1
    if a[i] + b[i] == "AG":
        cnt[2] += 1
    if a[i] + b[i] == "GA":
        cnt[3] += 1
    if a[i] + b[i] == "AT":
        cnt[4] += 1
    if a[i] + b[i] == "TA":
        cnt[5] += 1
    if a[i] + b[i] == "CG":
        cnt[6] += 1
    if a[i] + b[i] == "GC":
        cnt[7] += 1
    if a[i] + b[i] == "CT":
        cnt[8] += 1
    if a[i] + b[i] == "TC":
        cnt[9] += 1
    if a[i] + b[i] == "GT":
        cnt[10] += 1
    if a[i] + b[i] == "TG":
        cnt[11] += 1

ans = 0

for i in range(6):
    x = min(cnt[i*2], cnt[i*2+1])
    ans += x
    cnt[i*2] -= x
    cnt[i*2+1] -= x

comb = [[0, 6, 3], [2, 1, 7], [0, 8, 5], [4, 1, 9], [2, 10, 5], [4, 3, 11], [6, 10, 9], [8, 7, 11]]

for a,b,c in comb:
    x = min(cnt[a], cnt[b], cnt[c])
    ans += x*2
    cnt[a] -= x
    cnt[b] -= x
    cnt[c] -= x

comb = [[0, 6, 10, 5], [0, 8, 3, 11], [2, 1, 10, 9], [2, 8, 3, 9], [2, 8, 7, 5], [4, 1, 7, 11], [4, 6, 3, 9], [4, 6, 7, 5]]

for a,b,c,d in comb:
    x = min(cnt[a], cnt[b], cnt[c], cnt[d])
    ans += x*3
    cnt[a] -= x
    cnt[b] -= x
    cnt[c] -= x
    cnt[d] -= x

print(ans)