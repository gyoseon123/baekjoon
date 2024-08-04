import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    score_a = 0
    score_b = 0
    minus = 0
    plus = 0
    for i in range(n):
        if a[i] == -1 and b[i] == -1:
            minus += 1
        elif a[i] == b[i]:
            plus += a[i]
        
        if a[i] == 0 and b[i] == 1:
            score_b += 1
        if a[i] == 1 and b[i] == -1:
            score_a += 1
        if a[i] == 1 and b[i] == 0:
            score_a += 1
        if a[i] == -1 and b[i] == 1:
            score_b += 1

    if plus > 0:
        if score_a > score_b:
            tmp = plus
            plus -= min(score_a - score_b, plus)
            score_b += min(score_a - score_b, tmp)
        else:
            tmp = plus
            plus -= min(score_b - score_a, plus)
            score_a += min(score_b - score_a, tmp)

        if score_a == score_b:
            x = plus//2 + plus%2
            score_a += x
            score_b += x - plus%2

    if minus > 0:
        if score_a > score_b:
            tmp = minus
            minus -= min(score_a - score_b, minus)
            score_a -= min(score_a - score_b, tmp)
        else:
            tmp = minus
            minus -= min(score_b - score_a, minus)
            score_b -= min(score_b - score_a, tmp)
        

    
        if score_a == score_b:
            print(score_a - abs(minus)//2 - abs(minus)%2)
        else:
            print(min(score_a, score_b))
    else:
        print(min(score_a, score_b))
    

            
        