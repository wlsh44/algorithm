#include <iostream>
#include <stack>

using namespace std;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        stack<char> s;
        string str;
        bool flag = true;

        cin >> str;
        for (auto c : str) {
            if (c == '(') {
                s.push(c);
            } else {
                if (s.empty()) {
                    flag = false;   
                    break;
                } else {
                    s.pop();
                }
            }
        }
        if (flag && s.empty()) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}