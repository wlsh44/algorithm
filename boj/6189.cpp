#include <iostream>
#include <stack>
#include <utility>

using namespace std;

void solve() {
    int arr[80003];
    stack<int> s;
    int n;
    long long res = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;

        cin >> num;
        arr[i] = num;
    }
    for (int i = 0; i < n; i++) {
        while (!s.empty() && s.top() <= arr[i]) {
            s.pop();
        }
        s.push(arr[i]);
        res += s.size() - 1;
    }
    cout << res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}