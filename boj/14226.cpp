#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int S;
int t;
bool visited[2001][2001];
queue<pair<int, int> > q;

void bfs() {
	t = 1;
	q.push(make_pair(1, 1));
	visited[1][1] = true;

	while (!q.empty()) {
		int size = q.size();

		while (size-- != 0) {
			pair<int, int> n = q.front();
			int s = n.first;
			int c = n.second;
			q.pop();

			if (s == S) {
				cout << t;
				return;
			}

			if (s <= 1000 && visited[s][s] == false && s > c) {
				q.push(make_pair(s, s));
				visited[s][s] = true;
			}
			if (s <= 1000 && visited[s + c][c] == false) {
				q.push(make_pair(s + c, c));
				visited[s + c][c] = true;
			}
			if (visited[s - 1][c] == false && s > c) {
				q.push(make_pair(s - 1, c));
				visited[s - 1][c] = true;
			}
		}
		t++;
	}
}

void solve() {
	cin >> S;

	bfs();
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}