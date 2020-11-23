#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int T;
int N;
long long sum;

// bool cmp(const pair<int, long long> &a, const pair<int, long long> &b) {
// 	if (a.first == b.first)
// 		return a.second < b.second;
// 	return a.first < b.first;
// }

// void solve() {
// 	//cin >> T;
	
// 	//while (T != 0) {
// 		vector<pair<int, long long> > v;

// 		//cin >> N;
// 		sum = 1;
// 		// for (int i = 0; i < N; i++) {
// 		// 	long long tmp;
			
// 		// 	cin >> tmp;
// 		// 	v.push_back(make_pair(0, tmp));
// 		// }
// 		v.push_back(make_pair(0, 2));
// v.push_back(make_pair(0, 10));
// v.push_back(make_pair(0, 3));
// v.push_back(make_pair(0, 8));
// v.push_back(make_pair(0, 14));



// 		while (v.size() != 1) {
// 			vector<pair<int, long long> > e;

// 			sort(v.begin(), v.end(), cmp);
// 			for (int i = 0; i < v.size() - 1; i += 2) {
// 				int quotient;
// 				long long remainder;

// 				quotient = v[i].first + v[i + 1].first + v[i].second * v[i + 1].second / 1000000007;
// 				remainder = v[i].second * v[i + 1].second % 1000000007;
// 				sum = (long long)(sum * remainder) % 1000000007;
// 				e.push_back(make_pair(quotient, remainder));
// 			}
// 			if (v.size() % 2 == 1)
// 				e.push_back(make_pair(v[v.size() - 1].first, v[v.size() - 1].second));
// 			v = e;
// 		}
// 		cout << sum << "\n";
// 	//	T--;
// 	//}
// }
#include <queue>

void solve() {
	cin >> T;
		
	while (T != 0) {
		priority_queue<long long, vector<long long>, greater<long long> > pq;

		cin >> N;
		sum = 1;
		for (int i = 0; i < N; i++) {
			long long tmp;
			
			cin >> tmp;
			pq.push(tmp);
		}
		while (pq.size() != 1) {
			long long num1;
			long long num2;

			num1 = pq.top();
			pq.pop();
			num2 = pq.top();
			pq.pop();
			sum = (sum * (num1 * num2 % 1000000007)) % 1000000007;
		cout << "num1: " << num1 << " num2: " << num2 << " " << sum << "\n";
			pq.push(num1 * num2); 
		}
		cout << sum << "\n";
		T--;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}