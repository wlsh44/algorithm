import sys, math

input = sys.stdin.readline

N = int(input())
arr = [list(map(lambda x: int(x) * 4, input().split())) for _ in range(N)]
dp = [[math.inf] * 6 for _ in range(N)]
time = [[math.inf] * 6 for _ in range(N)]
time[0][0] = arr[0][0]
dp[0][0] = arr[0][1]

for i in range(1, N):
	for cnt in range(6):
		if cnt == 0:
			dp[i][cnt] = min(dp[i - 1]) + arr[i][1]
			time[i][cnt] = arr[i][0]
		else:
			if time[i - 1][cnt - 1] < 120 * 4:
				if cnt == 1:
					dp[i][cnt] = dp[i - 1][cnt - 1] + arr[i][1] * 0.5
				else:
					dp[i][cnt] = dp[i - 1][cnt - 1] + arr[i][1] * 0.25
				time[i][cnt] = time[i - 1][cnt - 1] + arr[i][0]
print(f"{min(dp[N - 1]) / 4:.2f}")


