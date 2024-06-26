table = {'@':'a', '[':'c', '!':'i', ';':'j', '^':'n', '0':'o', '7':'t', '\\\\\'':'w', '\\\'':'v'}
n = int(input())
for _ in range(n):
    s = input()
    alp = sum([i.isalpha() for i in s])
    for k,v in table.items():
        s = s.replace(k,v)
    if len(s)//2 >= alp:
        s = 'I don\'t understand'
    print(s)
