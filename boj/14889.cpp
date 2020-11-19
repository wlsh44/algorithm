#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int n;
int arr[20][20];
vector<int> player;
vector<int> check;
int res;
int s_sum;
int l_sum;

void solve() {
	cin >> n;

	res = INT_MAX;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		if (i < n / 2) {
			player.push_back(0);
			check.push_back(0);
		}
		else {
			player.push_back(1);
			check.push_back(1);
		}
	}

	do {
		vector<int> start;
		vector<int> link;

		if (player == check)
			continue;
		l_sum = 0;
		s_sum = 0;
		for (int i = 0; i < n; i++) {
			if (player[i] == 0)
				start.push_back(i);
			else
				link.push_back(i);
		}

		for (int i = 0; i < n / 2 - 1; i++) {
			for (int j = i + 1; j < n / 2; j++) {
				s_sum += arr[start[i]][start[j]] + arr[start[j]][start[i]];
				l_sum += arr[link[i]][link[j]] + arr[link[j]][link[i]];
			}
		}
		res = min(res, abs(s_sum - l_sum));
		copy(player.begin(), player.end(), check.begin());
	} while (next_permutation(player.begin(), player.end()));
	cout << res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}