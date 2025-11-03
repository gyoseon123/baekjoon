import sys
input = sys.stdin.readline

def end():
    print(f"? {cycle - start%cycle} {start}", flush=True)
    answer = int(input())
    print(f"! {start} {answer}", flush=True)
    exit()

n = int(input())

print(f"? {n} 1", flush=True)

start = int(input())
pos = [-1]*(n+1)
pos[start] = 0
cycle = -1
for i in range(1, 500):
    print(f"? {i} {start}", flush=True)
    answer = int(input())
    if pos[answer] != -1:
        cycle = i
        end()
    pos[answer] = i

for i in range(500, n+1, 500):
    print(f"? {i} {start}", flush=True)
    answer = int(input())
    if pos[answer] != -1:
        cycle = i - pos[answer]
        end()