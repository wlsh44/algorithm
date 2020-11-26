#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

int N;
vector<int> v(26);
long long res;

void solve() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		string num;

		cin >> num;
		for (int j = 0; j < num.size(); j++) {
			v[num[j] - 'A'] += pow(10, num.size() - 1 - j); 
		}
	}
	sort(v.begin(), v.end(), greater<int>());
	for (int i = 0; i <= 9; i++) {
		res += v[i] * (9 - i);
	}
	cout << res;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}