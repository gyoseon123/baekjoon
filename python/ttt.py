n = int(input())
block = list(map(int, input().split()))
block.sort()
if n == 1:
    print(block[0])
else:
    print("%.7f" %(max(sum(block)/n, block[-2])))