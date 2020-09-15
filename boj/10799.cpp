#include <iostream>
#include <stack>

using namespace std;

int main() {
    int res;
    string str;
    stack<char> s;

    cin >> str;
    res = 0;
    for (auto c : str) {
        char tmp;

        if (c == '(') {
            s.push(c);
        } else {
            s.pop();
            if (tmp == '(') {
                res += s.size();
            } else {
                res += 1;
            }
        }
        tmp = c;
    }
    cout << res;
}