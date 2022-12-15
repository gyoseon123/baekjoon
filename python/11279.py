import sys
input = sys.stdin.readline

n = int(input())
heap = []
def insert(num):
    heap.append(num)
    child = len(heap)-1
    while child != 0 and num > heap[child//2]:
        heap[child], heap[child//2] = heap[child//2], heap[child]
        child = child//2

def delete():
    heap[0], heap[-1] = heap[-1], heap[0]
    print(heap.pop())
    parent = 0
    while parent < len(heap) - 1:
        child = parent*2
        if child+1 < len(heap) and heap[parent] < heap[child+1]:
            heap[parent], heap[child+1] = heap[child+1], heap[parent]
            parent = child+1
            continue
        if child+2 < len(heap) and heap[parent] < heap[child+2]:
            heap[parent], heap[child+2] = heap[child+2], heap[parent]
            parent = child+2
            continue

for i in range(n):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            delete()
    else:
        insert(num)

        
         