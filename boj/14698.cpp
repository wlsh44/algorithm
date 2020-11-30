#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int T;
int N;
long long sum;

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