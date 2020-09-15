#include <iostream>
#include <stack>
#include <utility>
using namespace std;

void solve() {
    stack<pair<int, int> > s;
    int n;

    cin >> n;
    for (int i = 1; i <= n; i++) {
        int num;

        cin >> num;
        while (!s.empty()) {
            if (s.top().first > num) {
                cout << s.top().second << " ";
                break;
            }
            s.pop();
        }
        if (s.empty()) {
            cout << 0 << " ";
        }
        s.push(make_pair(num, i));
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}