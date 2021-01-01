#include <iostream>
#include <utility>

using namespace std;

int T, N;

void solve() {
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		pair<int, int> dp[41];

		dp[0] = make_pair(1, 0);
		dp[1] = make_pair(0, 1);
		cin >> N;
		for (int i = 2; i <= N; i++) {
			dp[i] = make_pair(dp[i - 1].first + dp[i - 2].first, dp[i - 1].second + dp[i - 2].second);
		}
		cout << dp[N].first << " " << dp[N].second << "\n";
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}