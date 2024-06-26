n,m = map(int, input().split())
n += 1
m += 1
point = []
for i in range(1,n+1):
    for j in range(1,m+1):
        point.append((i,j))

def dis(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def is_same_line(x1,y1,x2,y2,x3,y3):
    if x1 == x2 and x2 == x3:
        return True
    elif y1 == y2 and y2 == y3:
        return True
    elif x1-x2 != 0 and x2-x3 != 0:
        if (y1-y2)/(x1-x2) == (y2-y3)/(x2-x3):
            return True
    else:
        return False


used = set()
for i in range(n*m):
    for j in range(i+1,n*m):
        for k in range(j+1,n*m):
            point1 = point[i]
            point2 = point[j]
            point3 = point[k]
            if is_same_line(point1[0],point1[1],point2[0],point2[1],point3[0],point3[1]):
                continue
            tri = [dis(point1[0],point1[1],point2[0],point2[1]),dis(point2[0],point2[1],point3[0],point3[1]),dis(point3[0],point3[1],point1[0],point1[1])]
            used.add(tuple(sorted(tri)))
print(len(used))