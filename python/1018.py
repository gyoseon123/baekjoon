import sys
input = sys.stdin.readline
def check_chess(arr):
    count1 = 0
    count2 = 0
    start = arr[0][0]
    if start == 'W':
        check = 0
    else:
        check = 1
    w = 'WBWBWBWB'
    b = 'BWBWBWBW'
    for i in arr:
        for j in range(8):
            if check%2 == 0:
                if i[j] != w[j]:
                    count1 += 1
                else:
                    count2 += 1
            else:
                if i[j] != b[j]:
                    count1 += 1
                else:
                    count2 += 1
        check += 1
    return min(count1, count2)
result = []
y,x = map(int, input().split()) # x = 가로 y = 세로
l = [list(input().split()) for _ in range(y)]
k = 0
for i in range(y-7):
    xl = l[i:i+8]
    for j in range(x-7):
        new_l = []
        for k in xl:
            new_l.append(k[0][j:j+8])
        result.append(check_chess(new_l))
print(min(result))