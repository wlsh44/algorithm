N, M = map(int, input().split())

coins = []
arr = [10e9] * 101
for _ in range(N):
    coin = int(input())
    arr[coin] = 1
    coins.append(coin)

for coin in coins:
    for i in range(coin, M + 1):
        if arr[i - coin] != 10e9:
            arr[i] = min(arr[i], arr[i - coin] + 1)
print(arr[M] if arr[M] != 10e9 else -1)
