import sys
input = sys.stdin.readline

a = int(input())
str = []
for i in range(a):
    str.append(input().rstrip())

str = list(set(str)) # 중복제거

str.sort(key = lambda x : (len(x), x)) # 길이, 사전순 정렬

for i in str:
    print(i)
