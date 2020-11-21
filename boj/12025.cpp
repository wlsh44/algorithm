#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

// string pwd;
// double k;
// vector<int> changed;
// vector<string> dp;
// string new_pwd;
// int n;

// void solve() {
// 	cin >> pwd;
// 	cin >> k;

// 	new_pwd = pwd;
// 	for (int i = pwd.length() - 1; i >= 0; i--) {
// 		if (pwd[i] == '6' || pwd[i] == '1') {
// 			new_pwd[i] = '1';
// 			changed.push_back(i); 
// 		} else if (pwd[i] == '7' || pwd[i] == '2') {
// 			new_pwd[i] = '2';
// 			changed.push_back(i);
// 		}
// 	}
// 	if (k > pow(2, pwd.length()))
// 		cout << -1;
// 	else {
// 		dp.push_back(new_pwd);
// 		for (int i = 1; i < k; i++) {
// 			if (i == pow(2, n)) {
// 				dp.push_back(new_pwd);
// 				n++;
// 			} else {
// 				dp.push_back(dp[pow(2, n) - i]);
// 			}
// 			if (dp[i][changed[n - 1]] == '1') dp[i][changed[n - 1]] = '6';
// 			else dp[i][changed[n - 1]] = '7';
// 		}
// 		cout << dp[k - 1];
// 	}
// }
// 111111111111111111111111111111111111111111111111111111111111111
// 9223372036854775807
string pwd;
string new_pwd;
long long k;
vector<int> changed;

void solve() {
	int i = 0;
	
	cin >> pwd;
	cin >> k;

	new_pwd = pwd;
	for (int i = pwd.length() - 1; i >= 0 ; i--) {
		if (pwd[i] == '6' || pwd[i] == '1' || pwd[i] == '2' || pwd[i] == '7') {
			if (pwd[i] == '6')
				new_pwd[i] = '1';
			else if (pwd[i] == '7')
				new_pwd[i] = '2';
			changed.push_back(i);
		}
	}
	if (k > pow(2, changed.size())) {
		cout << -1;
		return ;
	}
	if (changed.size() == 0) {
		if (k != 1) {
			cout << -1;
			return ;
		}
		cout << pwd;
		return ;
	}
	k--;
	do {
		if (k % 2 != 0) {
			if (new_pwd[changed[i]] == '1') {
				new_pwd[changed[i]] = '6';
			} else if (new_pwd[changed[i]] == '2') {
				new_pwd[changed[i]] = '7';
			}
		}
		i++;
		k /= 2;
	} while (k != 0);
	cout << new_pwd;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}