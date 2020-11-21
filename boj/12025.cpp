#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

/*1256
1251 = 0000
~
0001
0100
0101
1000
1001
1100
1101
6756 = 1101
*/
string pwd;
double k;
vector<int> changed;
vector<string> dp;
string new_pwd;
int n;

void solve() {
	cin >> pwd;
	cin >> k;

	new_pwd = pwd;
	for (int i = pwd.length() - 1; i >= 0; i--) {
		if (pwd[i] == '6' || pwd[i] == '1') {
			new_pwd[i] = '1';
			changed.push_back(i); 
		} else if (pwd[i] == '7' || pwd[i] == '2') {
			new_pwd[i] = '2';
			changed.push_back(i);
		}
	}
	if (k > pow(2, pwd.length()))
		cout << -1;
	else {
		dp.push_back(new_pwd);
		for (int i = 1; i < k; i++) {
			if (i == pow(2, n)) {
				dp.push_back(new_pwd);
				n++;
			} else {
				dp.push_back(dp[pow(2, n) - i]);
			}
			if (dp[i][changed[n - 1]] == '1') dp[i][changed[n - 1]] = '6';
			else dp[i][changed[n - 1]] = '7';
		}
		cout << dp[k - 1];
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}