#include <iostream>

using namespace std;

int main() {
	int T;
	int a, b;
	int res;

	cin >> T;
	for (int t = 0; t < T; t++) {
		res = 1;
		cin >> a >> b;
		for (int i = 0; i < b; i++) {
			res = (res * a) % 10;
			if (res == 0)
				res = 10;
		}
		cout << res << endl;
	}

}