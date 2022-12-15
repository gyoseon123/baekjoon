a,b = map(int, input().split())
x = 0
m_1 = [1,3,5,7,8,10,12]
m_2 = [4,6,9,11]
while a != 1:
    if a-1 == 2:
        x += 28
    if a-1 in m_1:
        x += 31
    if a-1 in m_2:
        x += 30
    a -= 1
x += b
if x%7 == 1:
    print('MON')
if x%7 == 2:
    print('TUE')
if x%7 == 3:
    print('WED')
if x%7 == 4:
    print('THU')
if x%7 == 5:
    print('FRI')
if x%7 == 6:
    print('SAT')
if x%7 == 0:
    print('SUN')