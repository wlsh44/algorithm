#include <iostream>

using namespace std;

int arr[10];
int N;

void solve() {
	cin >> N;

	for (int i = 1; i <= N; i++) {
		int num;
		int cnt;

		cnt = 0;
		cin >> num;
		for (int j = 0; j < N; j++) {
			if (cnt == num && arr[j] == 0) {
				arr[j] = i;
				break;
			} else if (arr[j] == 0)
				cnt++;
		}
	}
	for (int i = 0; i < N; i++) {
		cout << arr[i] << " ";
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}