#include <iostream>
#include <queue>

using namespace std;

int N, E;
int graph[101][101];
bool visited[101];

int bfs(int n) {
	int res;
	queue<int> q;

	res = 0;
	q.push(n);
	visited[n] = true;
	while (!q.empty()) {
		int v = q.front(); q.pop();

		res++;
		for (int i = 1; i <= N; i++) {
			if (!visited[i] && graph[v][i]) {
				visited[i] = true;
				q.push(i);
			}
		}
	}
	return (res);
}

void solve() {
	int res;

	res = 0;
	cin >> N >> E;

	for (int i = 0; i < E; i++) {
		int s, e;

		cin >> s >> e;
		graph[s][e] = 1;
		graph[e][s] = 1;
	}
	cout << bfs(1) - 1;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}