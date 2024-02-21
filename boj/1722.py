import sys, math


input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

num = arr[0]
arr = [arr[i] for i in range(1, len(arr))]


def find_iter(n, k):
    if n == 0:
        return

    res = k // math.factorial(n - 1) + 1
    print(res, end=" ")
    find_iter(n - 1, k - res)



if num == 1:
    order = arr[0]

    i = 0
    ans = [0] * N

    print(*ans)
else:
    ans = 1
    visited = [False] * (N + 1)
    for i in range(N):
        cnt = 0
        j = 1
        while j <= N and arr[i] != j:
            if visited[j] is False:
                cnt += 1
            j += 1
        visited[i + 1] = True
        ans += math.factorial(N - i - 1) * cnt
    print(ans)
