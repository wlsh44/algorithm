#include <iostream>
#include <stack>

using namespace std;

void aa (stack<char> s) {
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}

void solve() {
    int i = 1;
    while (true) {
        stack<char> s;
        string str;
        bool err = false;

        getline(cin, str);
        if (str == ".") {
            break;
        }
        for (auto c : str) {
            if (c == '(' || c == '[') {
                s.push(c);
            } else if (c == ')') {
                if (!s.empty() && s.top() == '(') {
                    s.pop();
                } else {
                    err = true;
                    break;
                }
            } else if (c == ']') {
                if (!s.empty() && s.top() == '[') {
                    s.pop();
                } else {
                    err = true;
                    break;
                }
            }
        }
        if (!err && s.empty()) {
            cout << "yes\n";
        } else {
            cout << "no\n";
        }
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}