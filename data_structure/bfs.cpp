#include <iostream>
#include <utility>
#include <queue>

using namespace std;

#define MAX 500

int graph[MAX][MAX];
bool visited[MAX][MAX];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int N, M;

void bfs_array() {
    queue<pair<int, int>> q;

    visited[0][0] = true;
    q.push({0, 0});
    while (!q.empty()) {
        pair<int, int> v = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = v.first + dx[i];
            int ny = v.second + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (graph[nx][ny] == 1 && visited[nx][ny] == false) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }
}

vector<vector<int>> graph2;
bool visited2[MAX];

void bfs_graph(int node) {
    queue<int> q;

    visited2[node] = true;
    q.push(node);
    while (!q.empty()) {
        int v = q.front(); q.pop();

        for (int i = 0; i < graph2[v].size(); i++) {
            if (visited2[graph2[v][i]] == false) {
                visited2[graph[v][i]] = true;
                q.push(graph[v][i]);
            }
        }
    }
}