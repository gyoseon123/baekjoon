# import sys
# from collections import deque
# t = int(sys.stdin.readline())
# for i in range(t):
#     sig = False
#     s = list(sys.stdin.readline().strip())
#     n = int(sys.stdin.readline().strip())
#     x = sys.stdin.readline().strip()
#     if x != '[]':
#         l = deque(list(map(int, x.strip('[],').split(','))))
#     else:
#         if s.count('D') == 0:
#             print('[]')
#         else:
#             print('error')
#         continue
#     for a,j in enumerate(s):
#         if j == 'R':
#             if len(s)-a >= 4:   #RDRD 최적화
#                 if s[a:a+4] == ['R','D','R','D']:
#                     if len(l) < 2:
#                         print('errer')
#                         continue
#                     l.pop()
#                     l.popleft()
#                     s[a+1],s[a+2],s[a+3] = 'X','X','X'
#                     continue
#             f = a
#             if f == len(s)-1:
#                 l.reverse()
#             else:
#                 while s[f+1] == 'R': #연속 R 최적화
#                     s[f+1] = 'X'
#                     f += 1
#                     if len(s) == f+1:
#                         break
#                 if (f-a)%2 == 1:
#                     pass
#                 else:
#                     l.reverse()
#         elif j == 'D':
#             if s.count('D') > n:
#                 print('errer')
#                 sig = True
#                 break
#             else:
#                 l.popleft()
#         else:
#             pass
#     if sig == False:
#         print('[' + ','.join(map(str,l)) + ']')

import sys
from collections import deque
t = int(sys.stdin.readline().strip())
for i in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().strip()
    if x != '[]':
        l = deque(list(map(int, x.strip('[],').split(','))))
    else:
        if p.count('D') == 0:
            print('[]')
            continue
        else:
            print('error')
            continue
    cnt = 0
    if p.count('D') > len(l):
        print('error')
        continue
    for j in p:
        if j == 'R':
            cnt += 1
        if j == 'D':
            if cnt%2 == 1:
                l.pop()
            else:
                l.popleft()
    if cnt%2 == 0:
        print('[' + ','.join(map(str,l)) + ']')
    else:
        l.reverse()
        print('[' + ','.join(map(str,l)) + ']')

