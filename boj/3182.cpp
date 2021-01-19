#include <iostream>
#include <algorithm>

using namespace std;

#define MAX 1000

bool visited[MAX];
int graph[MAX];
int N;
int maxNum, ans;

void solve()
{
	cin >> N;

	for (int i = 1; i <= N; i++)
		cin >> graph[i];

	for (int i = 1; i <= N; i++) {
		int num;
		int cur;

		cur = i;
		num = 0;
		fill(visited, visited + MAX, false);
		while (!visited[cur]) {
			visited[cur] = true;
			num++;
			cur = graph[cur];
		}
		if (num > maxNum) {
			maxNum = num;
			ans = i;
		}
	}
	cout << ans;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}