import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))

    left = 0
    right = 0
    ssum = a[0]
    ans = 0
    while True:
        if l <= ssum and ssum <= r:
            ans += 1
            left = right+1
            right += 1

            if right == n:
                break

            ssum = a[right]
        elif ssum > r:
            if left < right:
                ssum -= a[left]
                left += 1
            
            if l <= ssum and ssum <= r:
                ans += 1
                left = right+1
                right += 1
    
                if right == n:
                    break
                ssum = a[right]
                continue
            elif ssum < l:
                continue

            if left == right:
                left += 1
                right += 1

                if right == n:
                    break
                ssum = a[right]
        else:
            right += 1

            if right == n:
                break

            ssum += a[right]

    print(ans)

