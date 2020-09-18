#include <iostream>
#include <utility>
#include <queue>

using namespace std;

char graph[1000][1000];
bool visited[1000][1000];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int R, C;
queue<pair<int, int> > q;
queue<pair<int, int> > fq;

void bfs() {
    int fireNum = fq.size();
    int jihunNum = 1;
    int time = 0;
    int cnt;


    visited[q.front().first][q.front().second] = true;
    while (!q.empty()) {
        cnt = 0;
        time++;
        for (int i = 0; i < jihunNum; i++) {
            pair<int, int> v = q.front();

            q.pop();
            if (graph[v.first][v.second] == 'F')
                continue;
            for (int j = 0; j < 4; j++) {
                int nx = v.first + dx[j];
                int ny = v.second + dy[j];

                if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                    cout << time;
                    return ;
                } else {
                    if (graph[nx][ny] == '.' && visited[nx][ny] == false) {
                        q.push(make_pair(nx, ny));
                        visited[nx][ny] = true;
                        graph[nx][ny] = 'J';
                        cnt++;
                    }
                }
            }
        }
        jihunNum = cnt;
        cnt = 0;
        for (int i = 0; i < fireNum; i++) {
            pair<int, int> v = fq.front();

            fq.pop();
            for (int j = 0; j < 4; j++) {
                int nx = v.first + dx[j];
                int ny = v.second + dy[j];

                if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                    if (graph[nx][ny] == 'J' || (graph[nx][ny] != '#' && visited[nx][ny] == false)) {
                        fq.push(make_pair(nx, ny));
                        visited[nx][ny] = true;
                        graph[nx][ny] = 'F';
                        cnt++;
                    }
                }
            }
        }
        fireNum = cnt;
    }
    cout << "IMPOSSIBLE";
}

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        string str;
        int j = 0;

        cin >> str;
        for (auto c : str) {
            graph[i][j] = c;
            if (c == 'J') {
                q.push(make_pair(i, j));
            } else if (c == 'F') {
                fq.push(make_pair(i, j));
            }
            j++;
        }
    }
    bfs();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}