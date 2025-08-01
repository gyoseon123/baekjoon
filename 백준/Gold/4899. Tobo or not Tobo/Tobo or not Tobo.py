# ai test

from collections import deque

# 다이얼별 좌표 (인덱스)
dials = [
    [0, 1, 3, 4],  # A
    [1, 2, 4, 5],  # B
    [3, 4, 6, 7],  # C
    [4, 5, 7, 8],  # D
]

def rotate(state, dial, clockwise=True):
    state = list(state)
    indices = dials[dial]
    # 시계 방향
    if clockwise:
        state[indices[0]], state[indices[1]], state[indices[2]], state[indices[3]] = (
            state[indices[2]], state[indices[0]], state[indices[3]], state[indices[1]]
        )
    else:
        state[indices[0]], state[indices[1]], state[indices[2]], state[indices[3]] = (
            state[indices[1]], state[indices[3]], state[indices[0]], state[indices[2]]
        )
    return ''.join(state)

def solve_tobo(Y, arr):
    goal = '123456789'
    start = arr
    if start == goal:
        return 0
    visited = set()
    queue = deque()
    queue.append((start, 0))  # (상태, 회전 수)
    visited.add(start)
    while queue:
        cur, depth = queue.popleft()
        if depth >= Y:  # Y 초과하면 답 X
            continue
        for d in range(4):  # 4개 다이얼
            for cw in [True, False]:  # 시계/반시계
                nxt = rotate(cur, d, cw)
                if nxt == goal:
                    return depth + 1
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, depth + 1))
    return -1

case_num = 1
while True:
    line = input().strip()
    if line == '0000000000':
        break
    Y = int(line[0])
    arr = line[1:]
    res = solve_tobo(Y, arr)
    print(f"{case_num}. {res}")
    case_num += 1
