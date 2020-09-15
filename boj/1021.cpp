#include <iostream>
#include <deque>

using namespace std;

void solve() {
    deque<int> dq;
    int n;
    int m;
    int cnt = 0;

    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        dq.push_back(i);
    }
    for (int i = 0; i < m; i++) {
        int num;

        cin >> num;
        for (int j = 0; j < dq.size(); j++) {
            if (num == dq[j]) {
                int left = j;
                int right = dq.size() - j;
                if (left >= right) {
                    while (right-- > 0) {
                        dq.push_front(dq.back());
                        dq.pop_back();
                        cnt++;
                    }
                    dq.pop_front();
                } else {
                    while (left-- > 0) {
                        dq.push_back(dq.front());
                        dq.pop_front();
                        cnt++;
                    }
                    dq.pop_front();
                }
                break;
            }
        }
    }
    cout << cnt;
}



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}