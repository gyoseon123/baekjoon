import sys
input = sys.stdin.readline
n = int(input())
l = list(input().split())
word = set()
twice = set()
for i in l:
    if i not in word:
        word.add(i)
    else:
        twice.add(i)
result = set()
word = list(word)

for i in range(len(word)):
    for j in range(i+1,len(word)):
        result.add(chr(max(ord(word[i][0]), ord(word[j][1]))))
        result.add(chr(max(ord(word[i][1]), ord(word[j][0]))))
        
for i in twice:
    result.add(chr(max(ord(i[0]), ord(i[1]))))
print(len(result))
print(*sorted(list(result)))
