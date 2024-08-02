n = int(input())
text = [input() for _ in range(n)]

used = set()

for words in text:
    word = words.split()
    flg = False

    ans = ""
    for i in range(len(word)):
        w = word[i]
        if w[0].lower() not in used:
            used.add(w[0].lower())

            ans += f"[{w[0]}]" + w[1:] + ' ' + ' '.join(word[i+1:])
            flg = True
            break
        else:
            ans += w + ' '
    
    flg2 = False
    if not flg:
        for i in range(len(words)):
            if words[i] == ' ':
                continue
            if words[i].lower() not in used:
                used.add(words[i].lower())
                print(words[:i] + '[' + words[i] + ']' + words[i+1:])
                flg2 = True
                break
    else:
        print(ans)
        continue

    if not flg2:
        print(words)