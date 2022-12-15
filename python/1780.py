import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def find(k,arr,target):
    global count
    if k == 1:
        if paper[arr[2]][arr[0]] == target:
            count += 1
        return
    cnt = sum([i.count(target) for i in [m[arr[0]:arr[1]] for m in paper[arr[2]:arr[3]]]])
    size = k*k
    if cnt == size:
        count += 1
    else:
        for i in range(arr[0],arr[1],k//3):
            for j in range(arr[2],arr[3],k//3):
                find(k//3,(i,i+k//3,j,j+k//3),target)


for i in range(-1,2):
    count = 0
    find(n,(0,n,0,n),i)
    print(count)
















# import sys
# input = sys.stdin.readline
# x = int(input())
# paper = [list(map(int, input().split())) for _ in range(x)]
# def find(n,target,arr):
#     global count
#     if n == 1:
#         if paper[arr[0]][arr[3]] == target:
#             count += 1
#         return
#     size = n*n
#     cnt = sum([i.count(target) for i in [k[arr[0]:arr[1]] for k in paper[arr[2]:arr[3]]]])
#     if cnt == size:
#         count += 1
#     else:
#         for i in range(arr[0],arr[3],n//3):
#             for j in range(arr[0],arr[3],n//3):
#                 arr = (i,i+n//3,j,j+n//3)
#                 find(n//3,target,arr)
#         return


# count = 0
# find(x,1,(0,x,0,x))
# print(count)
