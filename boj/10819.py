N = int(input())
arr = list(map(int, input().split()))

ans = 0
visited = [False] * N

def dfs(route):
    global ans
    if len(route) == len(arr):
        tmp = 0
        for i in range(len(route) - 1):
            tmp += abs(route[i] - route[i + 1])
        ans = max(ans, tmp)
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            route.append(arr[i])
            dfs(route)
            visited[i] = False
            route.pop()


for num in arr:
    dfs([])
print(ans)
