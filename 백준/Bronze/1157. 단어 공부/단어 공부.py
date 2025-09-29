s = input()
s = s.lower()

cnt = [0]*26

for i in range(26):
    cnt[i] = s.count(chr(i + ord('a')))

ans = max(cnt)

if cnt.count(ans) > 1: print("?")
else:
    for i in range(26):
        if cnt[i] == ans:
            print(chr(i + ord('A')))