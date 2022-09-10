from collections import deque

N, K = map(int, input().split())

arr = deque([i for i in range(1, N + 1)])

print("<", end="")
for _ in range(N):
    for i in range(K - 1):
        arr.append(arr[0])
        arr.popleft()
    print(arr.popleft(), end="")
    if arr:
        print(", ", end="")
print(">")
