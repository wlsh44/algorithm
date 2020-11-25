#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int T;
int N;

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
	return a.first < b.first;
}

void solve() {
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		vector<pair<int, int> > v;
		int grade;
		int res;

		cin >> N;
		grade = N;
		res = N;
		for (int i = 0; i < N; i++) {
			int tmp1, tmp2;
			bool flag = false;

			cin >> tmp1 >> tmp2;
			v.push_back(make_pair(tmp1, tmp2));
		}
		sort(v.begin(), v.end());
		for (int i = 0; i < v.size(); i++) {
			if (v[i].second < grade)
				grade = v[i].second;
			else if (v[i].second > grade)
				res--;
		}
		cout << res << "\n";
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}