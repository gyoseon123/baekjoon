def make_window(word, width, height):
    ret = []
    if (len(word)&1 != width&1):
        first_line = "+" + ((width - 4 - len(word)) // 2)*"-" + "|" + word + "|" + ((width - 4 - len(word)) //2 + 1)*"-" + "+"
    else:
        first_line = "+" + ((width - 4 - len(word)) // 2)*"-" + "|" + word + "|" + ((width - 4 - len(word)) //2)*"-" + "+"
    ret.append(first_line)
    for _ in range(height - 2):
        mid_line = "|" + "."*(width-2) + "|"
        ret.append(mid_line)
    last_line = "+" + "-"*(width-2) + "+"
    ret.append(last_line)

    return ret

def is_alp(w):
    return "a" <= w <= "z"


m,n = map(int, input().split())
board = [list(input()) for _ in range(m)]
windows = []


for i in range(m):
    j = 0
    while (j < n):
        now = board[i][j]
        
        if now == "+":
            plus_pos = j
            while (board[i][j+1] == "-"):
                j += 1
            if board[i][j+1] == "+":
                j += 1
                pass
            else:
                start = plus_pos # 가로 찾기
                plus_pos += 1
                while (board[i][plus_pos+1] != "+"): plus_pos += 1
                width = plus_pos - start + 2

                s = i  # 세로 찾기 
                while (board[s+1][plus_pos+1] != "+"): s += 1
                height = s - i + 2


                j += 1 # 단어 찾는 과정
                s = ""
                while (is_alp(board[i][j+1])):
                    s += board[i][j+1]
                    j += 1

                windows.append((s, width, height))
                j = start+width-1
        j += 1


windows.sort()
result_board = [['.']*n for _ in range(m)]
for p in range(len(windows)):
    w = windows[p][1]
    h = windows[p][2]
    window = make_window(*windows[p])
    for i in range(h):
        for j in range(w):
            result_board[p+i][p+j] = window[i][j]


for l in result_board:
    print(''.join(l))

