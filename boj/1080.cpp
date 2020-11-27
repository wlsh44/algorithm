#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > v(50, vector<int>(50));
vector<vector<int> > v2(50, vector<int>(50));
int N, M;
int res = 2147483647;

void change(int row, int col) {
	for (int i = row; i < row + 3; i++) {
		for (int j = col; j < col + 3; j++) {
			if (v[i][j] == 0) v[i][j] = 1;
			else v[i][j] = 0;
		}
	}
}

void rec(int n, int row, int col) {
	if (v == v2) {
		if (res > n)
		res = n;
		return ;
	} else {
		if (col == M - 3) {
			col = 0;
			if (++row == N - 3) {
				cout << -1;
				return ;
			}
		}
		for (int i = col; i < M - 3; i++) {
			change(row, i);
			rec(n + 1, row, i + 1);
			change(row, i);
		}
	}
}

void solve() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int tmp;

			cin >> tmp;
			v[i][j] = tmp;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int tmp;

			cin >> tmp;
			v2[i][j] = tmp;
		}
	}
	rec(0, 0, 0);
	cout << res;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}