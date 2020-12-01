#include <iostream>
#include <algorithm>

using namespace std;
#define MAX 1000000

int T, N, M;
int note[MAX];

void solve() {
	cin >> T;

	while (T--) {
		cin >> N;

		for (int i = 0; i < N; i++) {
			int tmp;

			cin >> tmp;
			note[i] = tmp;
		}
		sort(note, note + N);
		cin >> M;

		for (int i = 0; i < M; i++) {
			int tmp;

			cin >> tmp;
			if (binary_search(note, note + N, tmp))
				cout << 1;
			else 
				cout << 0;
			cout << "\n";
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}