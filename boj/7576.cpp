#include <iostream>
#include <utility>
#include <queue>

using namespace std;

int graph[1000][1000];
bool visited[1000][1000];
queue<pair<int, int> > q;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int n, m;

void bfs() {
    int day = 0;
    int yesterdayNum = q.size();
    int cnt;
    bool flag;
    pair<int, int> v = q.front();

    visited[v.first][v.second] = true;
    while (!q.empty()) {
        cnt = 0;
        flag = false;
        while (yesterdayNum-- > 0) {
            v = q.front();
            q.pop();
            for (int i = 0; i < 4; i++) {
                int nx = v.first + dx[i];
                int ny = v.second + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (graph[nx][ny] == 0 && visited[nx][ny] == false) {
                        graph[nx][ny] = 1;
                        q.push(make_pair(nx, ny));
                        visited[nx][ny] = true;
                        cnt++;
                        flag = true;
                    }
                }
            }
        }
        yesterdayNum = cnt;
        if(flag) {
            day++;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 0) {
                cout << -1;
                return ;
            }
        }
    }
    cout << day;
}

void solve() {
    cin >> m >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int num;

            cin >> num;
            graph[i][j] = num;
            if (num == 1) {
                q.push(make_pair(i, j));
            }
        }
    }
    bfs();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}