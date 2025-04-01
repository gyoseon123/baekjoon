while True:
    try:
        n = int(input())
        num = 1
        cnt = 1
        while num%n != 0:
            num = (num*10+1)%n
            cnt += 1
        print(cnt)
    except:
        break