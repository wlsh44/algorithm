#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int graph[502][502];
int visited[502][502];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int n, m;


void bfs(int x, int y) {
    queue<pair<int, int> > q;

    q.push(make_pair(x, y));
    visited[x][y] = true;
    while (!q.empty()) {
        pair<int, int> v = q.front();

        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = v.first + dx[i];
            int ny = v.second + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (graph[nx][ny] != 0 && visited[nx][ny] == false) {
                    graph[nx][ny] = graph[v.first][v.second] + 1;
                    visited[nx][ny] = true;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
    cout << graph[n - 1][m - 1];
}

void solve() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string str;

        cin >> str;
        for (int j = 0; j < m; j++) {
            graph[i][j] = str[j] - '0';
        }
    }
    bfs(0, 0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
}