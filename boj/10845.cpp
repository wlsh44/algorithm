#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    queue<int> q;

    cin >> n;
    for (int i = 0; i < n; i++) {
        string str;
        
        cin >> str;
        if (str == "push") {
            int num;

            cin >> num;
            q.push(num);
        } else if (str == "pop") {
            if (!q.empty()) {
                cout << q.front() << "\n";
                q.pop();
            } else {
                cout << -1 << "\n";
            }
        } else if (str == "size") {
            cout << q.size() << "\n";
        } else if (str == "empty") {
            int num =  q.empty() ? 1 : 0;
            cout << num << "\n";
        } else if (str == "front") {
            if (!q.empty()) {
                cout << q.front() << "\n";
            } else {
                cout << -1 << "\n";
            }
        } else if (str == "back") {
            if (!q.empty()) {
                cout << q.back() << "\n";
            } else {
                cout << -1 << "\n";
            }
        }
    }
}