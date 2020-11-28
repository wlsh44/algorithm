#include <iostream>
#include <queue>

using namespace std;

long long res;
int N;

void solve () {
	priority_queue<int> plus;
	priority_queue<int, vector<int>, greater<int> > minus;
	//int minus, zero, plus;

	cin >> N;
	for (int i = 0; i < N; i++) {
		int num;

		cin >> num;
		if (num <= 0) minus.push(num);
		else if (num == 1) res++;
		else plus.push(num);
	}

	while (!plus.empty()) {
		int n1, n2;

		n1 = plus.top();
		plus.pop();
		if (plus.empty()) {
			res += n1;
		} else {
			n2 = plus.top();
			plus.pop();
			res += n1 * n2;
		}
	}
	while (!minus.empty()) {
		int n1, n2;

		n1 = minus.top();
		minus.pop();
		if (minus.empty()) {
			res += n1;
		} else {
			n2 = minus.top();
			minus.pop();
			res += n1 * n2;
		}

	}
	cout << res;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}
