def test(n):
    if n == 0:
        return
    print(n)
    test(n-1)

test(10)