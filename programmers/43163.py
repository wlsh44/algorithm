from collections import deque


def bfs(root, graph, visited, target):
    q = deque([root])
    cnt = 0

    while q:
        for i in range(len(q)):
            v = q.popleft()
            if v == target:
                return cnt
            for key in graph[v]:
                if key not in visited:
                    visited[key] = True
                    q.append(key)
        cnt += 1
    return 0


def solution(begin, target, words):
    answer = 0
    graph = {}
    visited = {begin: True}
    words = [begin] + words
    for word in words:
        graph[word] = []
    for key in words:
        for val in words:
            cnt = 0
            for key_c, val_c in zip(key, val):
                if key_c != val_c:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1:
                graph[key].append(val)
    answer += bfs(begin, graph, visited, target)
    return answer