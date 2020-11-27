#include <iostream>
#include <vector>

using namespace std;

vector<string> v;
vector<string> v2;
int N, M;
int res;

void change(int row, int col) {
	for (int i = row; i < row + 3; i++) {
		for (int j = col; j < col + 3; j++) {
			if (v[i][j] == '0') v[i][j] = '1';
			else v[i][j] = '0';
		}
	}
	res++;
}

void solve() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		string tmp;

		cin >> tmp;
		v.push_back(tmp);
	}
	for (int i = 0; i < N; i++) {
		string tmp;

		cin >> tmp;
		v2.push_back(tmp);
	}

	for (int i = 0; i < N - 2; i++) {
		for (int j = 0; j < M - 2; j++) {
			if (v[i][j] != v2[i][j]) 
				change(i, j);
		}
	}
	if (v == v2)
		cout << res;
	else 
		cout << -1;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}