import heapq, sys


input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = {i: [] for i in range(1, V + 1)}
dist = [sys.maxsize for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    # graph[v].append((u, w))


def dijkstra(graph, start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        # 현재 노드가 처리된 적이 있는 노드인 경우 무시
        if dist[cur_node] < cur_dist:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cur_dist + cost
            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(q, (new_cost, node))


dijkstra(graph, start)
for i in range(1, V + 1):
    if dist[i] < sys.maxsize:
        print(dist[i])
    else:
        print("INF")
"""
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""