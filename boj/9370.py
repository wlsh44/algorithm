import sys, heapq

input = sys.stdin.readline


def dijkstra(graph, start):
    dist = [INF for _ in range(len(graph) + 1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (dist[start], start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cost + cur_cost
            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(q, (new_cost, node))
    return dist


INF = int(1e9)

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    s, g, h = map(int, input().split())
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    candidates = [int(input()) for _ in range(t)]
    res = []
    for candidate in candidates:
        start_s = dijkstra(graph, s)
        start_g = dijkstra(graph, g)
        start_h = dijkstra(graph, h)
        if start_s[candidate] == start_s[g] + start_g[h] + start_h[candidate] or \
            start_s[candidate] == start_s[h] + start_h[g] + start_g[candidate]:
            res.append(candidate)
    res.sort()
    print(*res)


