def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b, a%b)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n-1):
        b.append(gcd(a[i], a[i+1]))

    if list(sorted(b[1:])) == b[1:] or list(sorted(b[:n-2])) == b[:n-2]:
        print("YES")
        continue

    # print(b)



    now = b[0]
    flag = False
    for i in range(1,n-1):
        next = b[i]
        if next < now:
            flag = True
            first_de = i
            break
        now = next
    else:
        print("YES")
        continue
    
    if flag:
        rem = first_de+1
        new_a = []
        for i in range(n):
            if i != rem:
                new_a.append(a[i])
        
        new_b = []
        for i in range(n-2):
            new_b.append(gcd(new_a[i], new_a[i+1]))
        
        if list(sorted(new_b)) == new_b:
            print("YES")
            continue

        rem = first_de
        new_a = []
        for i in range(n):
            if i != rem:
                new_a.append(a[i])
        
        new_b = []
        for i in range(n-2):
            new_b.append(gcd(new_a[i], new_a[i+1]))
        
        if list(sorted(new_b)) == new_b:
            print("YES")
            continue


        rem = first_de-1
        new_a = []
        for i in range(n):
            if i != rem:
                new_a.append(a[i])
        
        new_b = []
        for i in range(n-2):
            new_b.append(gcd(new_a[i], new_a[i+1]))
        
        if list(sorted(new_b)) == new_b:
            print("YES")
        else:
            print("NO")

        



    