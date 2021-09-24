N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
ans = []
idx = 0
for i in range(N):
    idx += K - 1
    if idx >= len(arr):
        idx = idx % len(arr)
    ans.append(str(arr.pop(idx)))
print("<", ", ".join(ans), ">", sep='')
