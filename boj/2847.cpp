#include <iostream>
#include <vector>
using namespace std;

int N;
int res;
vector<int> score;

void solve() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		int tmp;

		cin >> tmp;
		score.push_back(tmp);
	}
	for (int i = N - 1; i >= 1; i--) {
		if (score[i] <= score[i - 1]) {
			res += score[i - 1] - score[i] + 1;
			score[i - 1] = score[i] - 1;
		}
	}
	cout << res;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}