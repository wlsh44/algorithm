#include <iostream>
#include <utility>
#include <stack>
#include  <vector>

using namespace std;

#define MAX 500

int graph[MAX][MAX];
bool visited[MAX][MAX];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int N, M;

int dfs_array(pair<int, int> n) {
    stack<pair<int, int>> s;

    visited[n.first][n.second] = true;
    s.push(n);
    while (!s.empty()) {
        pair<int, int> v = s.top(); s.pop();

        for (int i = 0; i < 4; i++) {
            int nx = v.first + dx[i];
            int ny = v.second + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (graph[nx][ny] == 1 && visited[nx][ny] == false) {
                    visited[nx][ny] = true;
                }
            }
        }
    }
}

vector<vector<int>> graph2;
bool visited2[MAX];

void dfs_graph(int n) {
    visited2[n] = true;

    for (int i = 0; i < graph2[n].size(); i++)
    {
        if (visited2[graph2[n][i]] == false)
            dfs_graph(graph2[n][i]);
    }
}