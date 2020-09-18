#include <iostream>
#include <queue>

using namespace std;

#define N 100001

bool visited[N];
int n, k;

void bfs(int n) {
    queue<int> q;
    int num = 0;
    int cnt = 1;
    int tmp;

    visited[n] = true;
    q.push(n);
    while (!q.empty()) {
        tmp = 0;
        num++;
        for (int i = 0; i < cnt; i++) {
            int v = q.front();

            q.pop();
            for (int j = 0; j < 3; j++) {
                int nx = v;
                switch (j) {
                    case 0:
                        nx++;
                        break;
                    case 1:
                        nx--;
                        break;
                    case 2:
                        nx *= 2;
                        break;
                }
                if (nx >= 0 && nx < N) {
                    if (nx == k) {
                        cout << num;
                        return ;
                    } else if (visited[nx] == false) {
                        visited[nx] = true;
                        q.push(nx);
                        tmp++;
                    }
                }
            }
        }
        cnt = tmp;
    }
}

void solve() {
    cin >> n >> k;
    if (n == k) {
        cout << 0;
    } else {
        bfs(n);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}