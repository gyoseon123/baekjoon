import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    
    lp = 0
    rp = 0
    ret = []
    
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            ret.append(left[lp])
            lp += 1
        else:
            ret.append(right[rp])
            rp += 1
    
    while lp < len(left):
        ret.append(left[lp])
        lp += 1
    
    while rp < len(right):
        ret.append(right[rp])
        rp += 1
    
    return ret
    
n = int(input())
print(*merge_sort([int(input()) for _ in range(n)]), sep='\n')