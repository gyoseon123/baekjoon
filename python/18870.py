while True:
    n = input()
    n = n.lower()
    if n == '#':
        break
    print(n.count('a')+n.count('i')+n.count('u')+n.count('e')+n.count('o'))