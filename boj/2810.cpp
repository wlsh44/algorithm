#include <iostream>

using namespace std;

void solve() {
	int N;
	string str;
	int res;
	int i;

	i = 0;
	res = 0;
	cin >> N >> str;
	while (i < N) {
		if (str[i] == 'S')
			res++;
		else if (str[i] == 'L') {
			res++;
			i++;
		}
		i++;
	}
	if (++res > str.length())
		cout << str.length();
	else
		cout << res;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}