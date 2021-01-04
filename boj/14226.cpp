#include <iostream>
#include <climits>
#include <queue>
#include <utility>

using namespace std;

int dp[2001][2001];
int S;
int t;
bool visited[2001][2001];


void bfs() {
queue<pair<int, int> > q;
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
	//cin >> S;
S=872;
	//fill(&dp[0][0], &dp[2000][2000], INT_MAX / 2);
	//dp[1][1] = 1;
	bfs();
	//cout << min_time;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}