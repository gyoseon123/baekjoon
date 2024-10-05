key = "QWERTYUIOPASDFGHJKLZXCVBNM"
s = input()
for w in s:
    if w.isupper():
        print(key[key.index(w)+1], end='')
    else:
        print(w, end='')
    
