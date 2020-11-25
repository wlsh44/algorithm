#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int T;
int N;
vector<pair<int, int> > v;

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
	return a.first > b.first;
}

void solve() {
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		int res;

		cin >> N;
		res = N;
		for (int i = 0; i < N; i++) {
			int tmp1, tmp2;
			bool flag = false;

			cin >> tmp1 >> tmp2;
			for (int j = 0; j < v.size(); j++) {
				if (tmp1 > v[j].first && tmp2 > v[j].second) {
					flag = true;
					break;
				} else if (tmp1 < v.[j].first && v.)
			}
			if (!flag)
				v.push_back(make_pair(tmp1, tmp2));
		}
		cout << v.size() << "\n";
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}