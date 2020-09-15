#include <iostream>

using namespace std;

const int MAX = 10005;
int stack[MAX];
int pos;

void push(int num) {
    stack[pos] = num;
    pos++;
}

int pop() {
    int res;

    if (pos != 0) {
        res = stack[pos - 1];
        stack[pos - 1] = 0;
        pos--;
    } else {
        res = -1;
    }
    return res;
}

int size() {
    return pos;
}

int empty() {
    return pos == 0 ? 1 : 0;
}

int top() {
    return pos != 0 ? stack[pos - 1] : -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;

    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        int res;

        cin >> s;
        if (s == "push") {
            int num;
            cin >> num;
            push(num);
        } else {
            if (s == "pop") {
                res = pop();
            } else if (s == "top") {
                res = top();
            } else if (s == "size") {
                res = size();
            } else if (s == "empty") {
                res = empty();
            }
            cout << res << "\n";
        }
    }
}