import sys
input = sys.stdin.readline

def merge_sort(start, end):
    global answer, arr
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        temp = []
        x, y = start, mid + 1
        while x <= mid and y <= end:
            if arr[x] <= arr[y]:
                temp.append(arr[x])
                x += 1
            else:
                temp.append(arr[y])
                y += 1
                answer += (mid - x) + 1
        if x <= mid:
            temp = temp + arr[x:mid + 1]
        if y <= end:
            temp = temp + arr[y:end + 1]
        for i in range(len(temp)):
            arr[start+i] = temp[i]
        
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if set(a) != set(b):
        print("NO")
        continue

    arr = a[:]
    answer = 0
    merge_sort(0, n-1)
    ans1 = answer

    arr = b[:]
    answer = 0
    merge_sort(0,n-1)
    ans2 = answer

    if abs(ans1-ans2)%2 == 0:
        print("YES")
    else:
        print("NO")

