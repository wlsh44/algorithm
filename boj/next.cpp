#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <algorithm>
#define MAX 100
using namespace std;

int graph[MAX][MAX];
bool visited[100][100];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int N;
int res1, res2;

bool case1(int color, int x, int y) {
	if (color == graph[x][y])
		return (true);
	return (false);
}

bool case2(int color, int x, int y) {
	if (color == graph[x][y])
		return (true);
	else if ((color == 'R' && graph[x][y] == 'G') || (color == 'G' && graph[x][y] == 'R'))
		return (true);
	return (false);
}

void bfs(int x, int y, bool (*func)(int, int, int)) {
	queue<pair<int, int> > q;	
	
	visited[x][y] = true;
	q.push(make_pair(x, y));
	while (!q.empty()) {
		pair<int, int> v = q.front(); q.pop();
		int color;

		color = graph[v.first][v.second];
		for (int i = 0; i < 4; i++) {
			int x = v.first + dx[i];
			int y = v.second + dy[i];

			if (x >= 0 && x < N && y >= 0 && y < N && func(color, x, y) && !visited[x][y]) {
				visited[x][y] = true;
				q.push(make_pair(x, y));
			}
		}
	}
}

void solve() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		string str;

		cin >> str;
		for (int j = 0; j < N; j++) {
			graph[i][j] = str[j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!visited[i][j]) {
				bfs(i, j, case1);
				res1++;
			}
		}
	}
	fill(&visited[0][0], &visited[N - 1][N], 0);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!visited[i][j]) {
				bfs(i, j, case2);
				res2++;
			}
		}
	}
	cout << res1 << " " << res2;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}