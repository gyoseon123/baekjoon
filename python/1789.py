n = int(input())
cnt = 0
i = 1
while True:
    cnt += i
    i += 1
    if cnt > n:
        print(i-2)
        break