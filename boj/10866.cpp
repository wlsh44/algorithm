#include <iostream>
#include <deque>

using namespace std;

bool isEmpty(deque<int> dq) {
    if (dq.empty()) {
        cout << -1 << "\n";
        return true;
    } else {
        return false;
    }
}

void solve() {
    deque<int> dq;
    int n;

    cin >> n;
    for (int i = 0; i < n; i++) {
        string str;

        cin >> str;
        if (str == "push_back") {
            int num;

            cin >> num;
            dq.push_back(num);
        } else if (str == "push_front") {
            int num;

            cin >> num;
            dq.push_front(num);
        } else if (str == "front") {
            if (!isEmpty(dq))
                cout << dq.front() << "\n";
        } else if (str == "back") {
            if (!isEmpty(dq))            
                cout << dq.back() << "\n";
        } else if (str == "size") {
            cout << dq.size() << "\n";
        } else if (str == "empty") {
            if (dq.empty()) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        } else if (str == "pop_front") {
            if (!isEmpty(dq)) {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        } else if (str == "pop_back") {
            if (!isEmpty(dq)) {
                cout << dq.back() << "\n";                
                dq.pop_back();
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}