#include <iostream>
#include <deque>
using namespace std;

void solve() {
    string str;
    int T;

    cin >> T;
    for (int i = 0; i < T; i++) {
        deque<int> dq;
        string arr;
        string tmp = "";
        bool rev = false;
        bool err = false;
        int n;

        cin >> str >> n;
        cin >> arr;
        for (int j = 0; j < arr.length(); j++) {
            if (arr[j] >= '0' && arr[j] <= '9') {
                tmp += arr[j];
            } else if (arr[j] == ',' || arr[j] == ']') {
                if (tmp == "") {
                    if (n != 0)
                        err = true;
                    break;
                }
                dq.push_back(stoi(tmp));
                tmp = "";
            }
        }
        for (auto c : str) {
            if (c == 'R') {
                rev = !rev;
            } else if (c == 'D') {
                if (dq.empty()) {
                    err = true;
                    break;
                }
                if (rev == false) {
                    dq.pop_front();
                } else {
                    dq.pop_back();
                }
            }
        }
        if (err) {
            cout << "error\n";
        } else {
            cout << "[";
            if (rev == false) {
                while (!dq.empty()) {
                    cout << dq.front();
                    dq.pop_front();
                    if (!dq.empty())
                        cout << ",";
                }
            } else {
                while (!dq.empty()) {
                    cout << dq.back();
                    dq.pop_back();
                    if (!dq.empty())
                        cout << ",";
                }
            }
            cout << "]\n";
        }
        // for (int i = 0; i < dq.size(); i++) {
        //     cout << dq[i] << " ";
        // }
        // cout << endl;

    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}