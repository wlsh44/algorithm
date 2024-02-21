from collections import deque


A, B = map(int, input().split())
visited = {}

def bfs():
    q = deque([A])
    visited[A] = 1

    while q:
        num = q.popleft()

        if num == B:
            print(visited[B])
            exit()

        mul = num * 2
        plus1 = int(str(num) + '1')
        if mul not in visited and mul <= B:
            q.append(mul)
            visited[mul] = visited[num] + 1
        if plus1 not in visited and plus1 <= B:
            q.append(plus1)
            visited[plus1] = visited[num] + 1
    print(-1)


bfs()