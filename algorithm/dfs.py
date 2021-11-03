
"""
visited를 list가 아닌 dictionary로 만드는 이유는 in 연산자를 사용할 때 list는 O(N), dictionary는 O(1)이기 때문
"""

def dfs_adj_lst(graph, root):
    visited = {}
    s = [root]

    while s:
        v = s.pop()

        if v not in visited:
            visited[v] = True
            s += graph[v]
    return list(visited.keys())


graph = {1: [3, 4],
          2: [3, 4, 5],
          3: [1, 5],
          4: [1],
          5: [2, 6],
          6: [3, 5]}
root = 1

print(dfs_adj_lst(graph, root))