from collections import deque


"""
deque를 사용하는 이유는 list를 통해 list.pop(0)를 하면 시간복잡도가 O(N)이 나오기 때문
visited를 list가 아닌 dictionary로 만드는 이유는 in 연산자를 사용할 때 list는 O(N), dictionary는 O(1)이기 때문
"""

def bfs_adj_lst(graph, root):
    visited = {}
    q = deque([root])

    while q:
        v = q.popleft()

        if v not in visited:
            visited[v] = True
            q += graph[v]
    return list(visited.keys())


graph = {1: [3, 4],
          2: [3, 4, 5],
          3: [1, 5],
          4: [1],
          5: [2, 6],
          6: [3, 5]}
root = 1

print(bfs_adj_lst(graph, root))