import sys

input = sys.stdin.readline

N = int(input())

heap = [0]


def insert(val):
    heap.append(val)
    i = len(heap) - 1
    parent = i // 2

    while i > 1:
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
            parent = i // 2
        else:
            break


def delete():
    if len(heap) == 1:
        return 0
    heap[1], heap[-1] = heap[-1], heap[1]
    return heap.pop()


def heapify():
    parent = 1

    while len(heap) > 1:
        i = parent
        left = parent * 2
        right = parent * 2 + 1

        if left < len(heap) and heap[left] > heap[i]:
            i = left
        if right < len(heap) and heap[right] > heap[i]:
            i = right
        if i != parent:
            heap[i], heap[parent] = heap[parent], heap[i]
            parent = i
        else:
            break


for _ in range(N):
    num = int(input())

    if num == 0:
        print(delete())
        heapify()
    else:
        insert(num)