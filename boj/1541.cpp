#include <iostream>

using namespace std;

string expression;
string tmp;
int sum;
bool flag;

void solve() {
	cin >> expression;
	for (auto c : expression) {
		if (c == '+' || c == '-') {
			if (!flag) {
				sum += stoi(tmp);
				if (c == '-')
					flag = true;
			} else {
				sum -= stoi(tmp);
			}
			tmp.clear();
		} else {
			tmp += c;
		}
	}
	if (flag)
		cout << sum - stoi(tmp);
	else
		cout << sum + stoi(tmp);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}