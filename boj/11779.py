import sys, heapq


input = sys.stdin.readline
N = int(input())
M = int(input())

graph = {i: [] for i in range(1, N + 1)}
dist = [(int(1e9), [])] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    dist[start] = (0, [start])
    heapq.heappush(q, (0, start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if dist[cur_node][0] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cost + cur_cost
            if new_cost < dist[node][0]:
                _, path = dist[cur_node]
                new_path = path.copy()
                new_path.append(node)
                dist[node] = (new_cost, new_path)
                heapq.heappush(q, (new_cost, node))


s, e = map(int, input().split())
dijkstra(s)
print(dist[e][0])
print(len(dist[e][1]))
print(*dist[e][1])
