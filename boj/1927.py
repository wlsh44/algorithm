import sys

input = sys.stdin.readline

N = int(input())

min_heap = [0]


def move_up(idx, parent):
    if idx <= 1:
        return False
    if min_heap[idx] < min_heap[parent]:
        return True
    return False


def insert(val):
    min_heap.append(val)
    idx = len(min_heap) - 1
    parent = idx // 2
    while move_up(idx, parent):
        min_heap[idx], min_heap[parent] = min_heap[parent], min_heap[idx]
        idx = parent
        parent = idx // 2


def delete():
    idx = len(min_heap) - 1
    if idx == 0:
        return 0
    min_heap[1], min_heap[idx] = min_heap[idx], min_heap[1]
    return min_heap.pop()


def heapify():
    parent = 1

    while len(min_heap) > 1:
        idx = parent
        left = parent * 2
        right = parent * 2 + 1

        if left < len(min_heap) and min_heap[left] < min_heap[idx]:
            idx = left
        if right < len(min_heap) and min_heap[right] < min_heap[idx]:
            idx = right
        if idx != parent:
            min_heap[parent], min_heap[idx] = min_heap[idx], min_heap[parent]
            parent = idx
        else:
            break


for _ in range(N):
    num = int(input())

    if num == 0:
        print(delete())
        heapify()
    else:
        insert(num)
