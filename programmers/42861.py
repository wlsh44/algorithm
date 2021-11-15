import heapq


def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for cost in costs:
        graph[cost[0]].append([cost[2], cost[1]])
        graph[cost[1]].append([cost[2], cost[0]])

    visited[0] = True
    candidate = graph[0]
    heapq.heapify(candidate)

    while candidate:
        weight, v = heapq.heappop(candidate)
        if not visited[v]:
            visited[v] = True
            answer += weight

            for edge in graph[v]:
                if not visited[edge[1]]:
                    heapq.heappush(candidate, edge)
    return answer