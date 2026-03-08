from collections import deque

N = int(input())

arr = deque([i for i in range(1, N + 1)])

while len(arr) != 1:
    trash = arr.popleft()
    print(trash, end=" ")
    if len(arr) == 1:
        break
    arr.append(arr.popleft())
print(arr[0])
