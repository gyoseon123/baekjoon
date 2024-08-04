def solve():
    n,m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    col_a = []
    col_b = []
    for i in range(n):
        col_a.append(list(sorted(a[i])))
        col_b.append(list(sorted(b[i])))
    row_a = []
    row_b = []
    for i in range(m):
        sa = []
        sb = []
        for j in range(n):
            sa.append(a[j][i])
            sb.append(b[j][i])
        row_a.append(list(sorted(sa)))
        row_b.append(list(sorted(sb)))

    row_a.sort()
    row_b.sort()
    col_a.sort()
    col_b.sort()

    if row_a == row_b and col_a == col_b:
        print("YES")
    else:
        print("NO")



t = int(input())
for _ in range(t):
    solve()