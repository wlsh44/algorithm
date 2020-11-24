#include <iostream>
#include <cctype>
#include <deque>

using namespace std;

string expression;
string tmp;
deque<int> num;
deque<char> op;
int sum1;
int sum2;

void solve() {
	cin >> expression;
	for (auto c : expression) {
		if (isdigit(c)) {
			tmp += c;
		} else {
			if (c == '+' || c == '-') {
				op.push_back(c);
			}
			num.push_back(stoi(tmp));
			tmp.clear();
		}
	}
	num.push_back(stoi(tmp));
	sum1 += num.front();
	num.pop_front();

	while (num.size() != 0) {
		if (op.front() == '+') {
			sum1 +=	num.front();
			op.pop_front();
			num.pop_front();
		}
		else if (op.front() == '-'){
			do {
			sum2 += num.front();
			op.pop_front();
			num.pop_front();
			} while (op.front() == '+' || !op.empty());
		}
	}
	cout << sum1 - sum2;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}