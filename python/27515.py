import sys
import math
input = sys.stdin.readline
q = int(input())

def solve(arr):
    num = arr[:]
    for i in range(63):
        num[i+1] += num[i]//2
    for i in range(63,-1,-1):
        if num[i]:
            print(2**i)
            break
    else:
        print(0)

board = [0]*64
for _ in range(q):
    s = input().rstrip()
    if s[1] == '0':
        solve(board)
        continue
    if s[0] == '+':
        board[int(math.log(int(s[1:]),2))] += 1
    else:
        board[int(math.log(int(s[1:]),2))] -= 1
    solve(board)
