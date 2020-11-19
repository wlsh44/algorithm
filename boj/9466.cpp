#include <iostream>
#include <queue>
#include <utility>

using namespace std;

#define N 100000
int graph[N];
int n, T;

void solve() {
    cin >> T >> n;

    for (int tc = 0; tc < T; tc++) {
        //queue<pair<int, int> > q;
        int students = 0;

        for (int i = 1; i <= n; i++) {
            int num;

            cin >> num;
            graph[i] = num;
        }
        for (int i = 1; i <= n; i++) {
            pair<int, int> cur = make_pair(i, graph[i]);
            pair<int, int> nxt = make_pair(0, -1);
            pair<int, int> tmp = make_pair(0, -1);

            while (nxt.second != cur.first) {
                if ()
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}