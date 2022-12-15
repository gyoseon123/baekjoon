n = int(input())
cnt = 0
def n_queen(queen_state, line):
    global cnt
    if line == n:
        cnt += 1
        return
    for next_queen in range(1,n+1):
        sig = True
        for k,queen in enumerate(queen_state):
            dif = abs(next_queen-queen)
            if line-k == dif or dif == 0:
                sig = False
                break
        if sig:
            n_queen(queen_state+[next_queen], line+1)
    
for i in range(1,n+1):
    n_queen([i],1)
print(cnt)
