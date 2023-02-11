import sys
input = sys.stdin.readline
yut_count = 0
location = 0
sig_0 = True  # 기본상태
sig_1 = False  # 오른쪽 위
sig_2 = False  # 왼쪽 위
sig_3 = False  # 중간
result = False
while yut_count < 10:
    s = input().rstrip()
    yut = s.count('0')
    if yut < 4 and yut > 0:
        location += yut
        yut_count += 1
    elif yut == 4:
        location += 4
    else:
        location += 5
    if sig_0 and location == 5:
        sig_0 = False
        sig_1 = True
    elif sig_0 and location == 10:
        sig_0 = False
        sig_2 = True
    elif sig_1 and location == 8:
        sig_1 = False
        sig_3 = True
if sig_3 and location >= 12:
    result = True
if sig_2 and location >= 17:
    result = True
if sig_1 and location >= 17:
    result = True
if sig_0 and location >= 21:
    result = True
if result:
    print('WIN')
else:
    print('LOSE')
