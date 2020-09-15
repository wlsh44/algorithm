#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int graph[502][502];
int visited[502][502];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int n, m;
int paintNum;
int maxSize;

void bfs(int x, int y) {
    queue<pair<int, int> > q;
    int size = 0;

    q.push(make_pair(x, y));
    visited[x][y] = true;
    while (!q.empty()) {
        pair<int, int> v = q.front();
        q.pop();
        size++;

        for (int i = 0; i < 4; i++) {
            int nx = v.first + dx[i];
            int ny = v.second + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (graph[nx][ny] == 1 && visited[nx][ny] == false) {
                    visited[nx][ny] = true;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
    if (size > maxSize) {
        maxSize = size;
    }
}

void solve() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int x;

            cin >> x;
            graph[i][j] = x;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 1 && visited[i][j] == false) {
                bfs(i, j);
                paintNum++;
            }
        }
    }
    cout << paintNum << "\n" << maxSize;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
}