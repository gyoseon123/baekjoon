n = int(input())
count = 0
t_x,t_y = -1000000001,-1000000001
for i in range(n):
    x,y = map(int, input().split())
    if  x > t_x and y < t_y:
        count += y-t_y
    elif x < t_y:
        pass
    else:
        count += y-x
        print(count)
    t_x,t_y = x,y
print(count)