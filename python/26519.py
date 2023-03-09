import sys
input = sys.stdin.readline
V,E,a = map(int, input().split())
line = []
for _ in range(E):
    X,Y,b,c = map(int, input().split())
    line.append((b,c,X,Y))
t1,t2 = map(int, input().split())

def cal_linear_func(b1,c1,b2,c2):
    if b1-b2 != 0:
        return (c2-c1)/(b1-b2)
    else:
        return False
interval = []
interval.append(t1)
for i in range(E):
    for j in range(i+1,E):
        line1 = line[i]
        line2 = line[j]
        root = cal_linear_func(line1[0], line1[1], line2[0], line2[1])
        if not root:
            continue
        if root[0]/root[1] > t1 and root[0]/root[1] < t2:
            interval.append(root)
interval.append(t2)
interval.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a) 
    b = find(b)

    if a == b: return

    if rank[a] > rank[b]:
        a,b = b,a
    parent[a] = b
    if rank[a] == rank[b]:
        rank[b] += 1

def find_mst(point):
    global parent
    global rank
    graph = []
    parent = [i for i in range(V+1)]
    rank = [0]*(V+1)
    for i in range(E):
        cost = line[i][0]*point + line[i][1]
        graph.append((cost,line[i][2], line[i][3], line[i][0], line[i][1]))
    graph.sort()
    result = [0,0]
    for c,a,b,n,m in graph:
        if find(a) != find(b):
            union(a,b)
            result[0] += n
            result[1] += m
    return result

def integral(a,b,value,degree):
    return [(b**(degree+1) - a**(degree+1))*value, degree+1]

def gcd(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def plus_fraction(f1,f2):
    u1,d1 = f1
    u2,d2 = f2
    d = d1*d2
    u = u1*d2+u2*d1
    gcd_du = gcd(d,u)
    d //= gcd_du
    u //= gcd_du
    return [u,d]

p = 10**9+7
dx = 1/100000000
ans = 0
ans = integral(t1,t2,a*(V-1),2)
for i in range(len(interval)-1):
    mst_cost = find_mst(interval[i]+dx)
    print(mst_cost)
    print(integral(interval[i], interval[i+1], mst_cost[0], 1), integral(interval[i], interval[i+1], mst_cost[1], 0))
    plus = plus_fraction(integral(interval[i], interval[i+1], mst_cost[0], 1), integral(interval[i], interval[i+1], mst_cost[1], 0))
    ans = plus_fraction(ans, plus)
print(interval)
