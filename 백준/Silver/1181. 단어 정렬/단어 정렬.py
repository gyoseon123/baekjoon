import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for _ in range(n)]

l = list(set(l)) # 중복제거

l.sort(key = lambda x : (len(x), x)) # 길이, 사전순 정렬

print(*l, sep='\n')