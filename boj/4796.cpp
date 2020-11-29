#include <iostream>

using namespace std;

void solve() {
	int L, P, V;
	int i;

	i = 1;
	while (true) {
		int res;

		cin >> L >> P >> V;
		if (L == 0 && P == 0 && V == 0)
			break;
		res = (V / P) * L;
		res += V % P > L ? L : V % P;
		cout << "Case " << i << ": " << res << "\n";
		i++;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}