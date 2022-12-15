c = input()
l = []
new_l = []
x = 0
for k,i in enumerate(c):
    if i == '-' or i == '+':
        l.append(c[x:k])
        l.append(c[k])
        x = k+1
l.append(c[x::])

def num_check(n):
    a = 0
    if n == '-' or n == '+':
        return n
    for i in n:
        if i != '0':
            break
        else:
            a += 1
    return n[a::]

for i in l:
    new_l.append(num_check(i))


check = False
for i,c in enumerate(new_l):
    if c == '-':
        if check == False:
            new_l[i] = ')-('
            check = True
        else:
            new_l[i] = ')-('
            check = False

print(eval('(' + ''.join(new_l) + ')'))
