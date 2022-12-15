def binsearch(array,target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return 1
        
        if array[mid] < target:
            start = mid+1
        
        else:
            end = mid-1
    return 0

a = int(input())
a_list = sorted(list(map(int, input().split())))
b = int(input())
b_list = list(map(int, input().split()))
for i in b_list:
    print(binsearch(a_list,i))

