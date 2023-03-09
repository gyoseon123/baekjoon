import sys
input = sys.stdin.readline
nums = (
    ('###','#.#','#.#','#.#','###'),
    ('..#','..#','..#','..#','..#'),
    ('###','..#','###','#..','###'),
    ('###','..#','###','..#','###'),
    ('#.#','#.#','###','..#','..#'),
    ('###','#..','###','..#','###'),
    ('###','#..','###','#.#','###'),
    ('###','..#','..#','..#','..#'),
    ('###','#.#','###','#.#','###'),
    ('###','#.#','###','..#','###')
)

n = int(input())
state = [list(input().rstrip()) for _ in range(5)]
able_nums = []
for i in range(n):
    ban_num = set()
    for j in range(3):
        for k in range(5):
            for l in range(10):
                if state[k][i*3+j+i] == '#' and nums[l][k][j] == '.':
                    ban_num.add(l)
    able_nums.append(ban_num^set(range(10)))
divide = 1
for num in able_nums:
    divide *= len(num)
    if len(num) == 0:
        print(-1)
        exit()

sum_num = 0
for i in range(n):
    sum_num += sum(able_nums[i])*(10**(n-i-1))*(divide/len(able_nums[i]))
else:
    print(f"{sum_num/divide:.5f}")