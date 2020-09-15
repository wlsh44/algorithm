#include <iostream>
#include <stack>

using namespace std;

void aa (stack<char> s) {
    while (!s.empty()) {
        if (s.top() == '(' || s.top() == '[')
            cout << s.top() << " ";
        else {
            cout << (int)s.top() << " ";
        }
        s.pop();
    }
    cout << endl;
}

void solve() {
    string str;
    stack<char> s;
    int cur = 0;
    bool err = false;

    cin >> str;
    for (auto c : str) {
        if (c == '(' || c == '[') {
            s.push(c);
        } else if (c == ')') {
            if (!s.empty()) {
                if (s.top() == '(') {
                    s.pop();
                    s.push(2);
                } else if (s.top() == '[') {
                    err = true;
                    break;
                } else {
                    int tmp = s.top();
                    s.pop();
                    if (s.top() != '(') {
                        err = true;
                        break;                        
                    }
                    s.pop();
                    tmp *= 2;
                    if (!s.empty()) {
                        tmp += s.top();
                        s.pop();
                    }
                    s.push(tmp);
                }
            }
        } else if (c == ']') {
            if (!s.empty()) {
                if (s.top() == '[') {
                    s.pop();
                    s.push(3);
                } else if (s.top() == '(') {
                    err = true;
                    break;
                } else {
                    int tmp = s.top();
                    s.pop();
                    if (s.top() != '[') {
                        err = true;
                        break;                        
                    }
                    s.pop();
                    tmp *= 3;
                    if (!s.empty()) {
                        tmp += s.top();
                        s.pop();
                    }
                    s.push(tmp);
                }
            }
        }
        aa(s);
    }
    cout << s.top();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}