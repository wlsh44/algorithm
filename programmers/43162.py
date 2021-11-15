from collections import deque


def bfs(n, computers, visited, root):
    q = deque([root])

    while q:
        v = q.popleft()

        if v not in visited:
            visited[v] = True
            for i in range(n):
                if computers[v][i] == 1 and i not in visited:
                    q.append(i)


def solution(n, computers):
    answer = 0
    visited = {}
    for i in range(n):
        if i not in visited:
            bfs(n, computers, visited, i)
            answer += 1

    return answer