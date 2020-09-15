#include <iostream>
#include <utility>
#include <queue>

using namespace std;

#define N 500

int graph[N][N];
bool visited[N][N];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int n, m;
int main() {
    queue<pair<int, int>> q;

    visited[0][0] = true;
    q.push({0, 0});
    while (!q.empty()) {
        pair<int, int> v = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = v.first + dx[i];
            int ny = v.second + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (graph[nx][ny] == 1 && visited[nx][ny] == false) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }
}