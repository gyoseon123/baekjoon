a = input().upper()
b = list(set(a))
c_list = []
for i in b:
    c = a.count(i)
    c_list.append(c)
if c_list.count(max(c_list)) > 1:
    print('?')
else:
    max_index = c_list.index(max(c_list))
    print(b[max_index])