#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int T, n, m, k;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int graph[52][52];
bool visited[52][52];

void bfs(int y, int x) {
    queue<pair<int, int> > q;
    
    visited[y][x] = true;
    q.push(make_pair(y, x));
    while (!q.empty()) {
        pair<int, int> v = q.front();

        q.pop();
        for (int i = 0; i < 4; i++) {
            int ny = v.first + dy[i];
            int nx = v.second + dx[i];

            if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
                if (graph[ny][nx] == 1 && visited[ny][nx] == false) {
                    q.push(make_pair(ny, nx));
                    visited[ny][nx] = true;
                }
            }
        }
    }
}

void solve() {
    int cnt;

    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> m >> n >> k;
        fill(&graph[0][0], &graph[n - 1][m], 0);
        fill(&visited[0][0], &visited[n - 1][m], 0);
        cnt = 0;
        for (int i = 0; i < k; i++) {
            int x, y;

            cin >> x >> y;
            graph[y][x] = 1;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1 && visited[i][j] == false) {
                    cnt++;
                    bfs(i, j);
                }
            }
        }
        cout << cnt << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}