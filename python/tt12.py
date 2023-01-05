s = input()
a = s[0]
cnt = 1
for i in s[1:]:
    if i == a:
        cnt += 1
    else:
        break
print(cnt)