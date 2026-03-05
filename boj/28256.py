from collections import deque

T = int(input())
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j, visited):
    visited[i][j] = True
    q = deque([(i, j)])

    cnt = 0
    while q:
        y, x = q.popleft()

        cnt += 1
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 3 and 0 <= nx < 3 and not visited[ny][nx] and arr[ny][nx] == 'O':
                visited[ny][nx] = True
                q.append((ny, nx))
    return cnt


for _ in range(T):
    arr = []
    visited = [[False] * 3 for _ in range(3)]
    for i in range(3):
        arr.append(list(input()))
    tmp = list(map(int, input().split()))

    ans = []
    for i in range(3):
        for j in range(3):
            if (i == 1 and j == 1) or arr[i][j] == 'X' or visited[i][j] is True:
                continue
            ans.append(bfs(i, j, visited))
    ans.sort()
    tmp = sorted(tmp[1:])
    print(1 if ans == tmp else 0)
