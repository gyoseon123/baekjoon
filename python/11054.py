n = int(input())
Ai = [0] + list(map(int, input().split()))
Ai_re = [0] + Ai[::-1]
dp_1 = [0] * (n+1)
dp_2 = [0] * (n+1) 
for i in range(1,n+1):
    m_1 = 0
    m_2 = 0
    for j in range(i):
        if Ai[j] < Ai[i]:
            if dp_1[j] > m_1:
                m_1 = dp_1[j]
        if Ai_re[j] < Ai_re[i]:
            if dp_2[j] > m_2:
                m_2 = dp_2[j]
    dp_1[i] = m_1+1
    dp_2[i] = m_2+1
dp_2.reverse()
dp_2 = [0] + dp_2
dp_2.pop()
m = 0
for i in range(n+1):
    if dp_1[i] + dp_2[i] > m:
        m = dp_1[i] + dp_2[i]
print(m-1)