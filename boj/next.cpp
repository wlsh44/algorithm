#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int graph[8][8];
bool visited[8][8];
int N, M;
int ans;
int minVirus = INT_MAX;

int bfs(pair<int, int> node)
{
	int virusNum;
	queue<pair<int, int>> q;

	virusNum = 0;
	if (visited[node.first][node.second])
		return (virusNum);
	q.push(node);
	visited[node.first][node.second] = true;
	while (!q.empty())
	{
		pair<int, int> v = q.front();
		q.pop();
		virusNum++;

		for (int i = 0; i < 4; i++)
		{
			int x = v.first + dx[i];
			int y = v.second + dy[i];

			if (x < N && x >= 0 && y < M && y >= 0 && !visited[x][y] && graph[x][y] != 1)
			{
				visited[x][y] = true;
				q.push(make_pair(x, y));
			}
		}
	}
	return (virusNum);
}

void solve()
{
	vector<pair<int, int>> blank;
	vector<pair<int, int>> virus;
	int wallCnt = 0;

	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> graph[i][j];
			if (graph[i][j] == 0)
			{
				blank.push_back(make_pair(i, j));
			}
			else if (graph[i][j] == 2)
			{
				virus.push_back(make_pair(i, j));
			}
			else
			{
				wallCnt++;
			}
		}
	}
	pair<int, int> x = make_pair(0, 0);
	pair<int, int> y = make_pair(0, 0);
	pair<int, int> z = make_pair(0, 0);

	for (int i = 0; i < blank.size(); i++)
	{
		graph[blank[i].first][blank[i].second] = 1;
		for (int j = i + 1; j < blank.size(); j++)
		{
			graph[blank[j].first][blank[j].second] = 1;
			for (int k = j + 1; k < blank.size(); k++)
			{
				int virusNum = 0;

				graph[blank[k].first][blank[k].second] = 1;
				fill(&visited[0][0], &visited[8][8], false);
				for (int v = 0; v < virus.size(); v++)
				{
					virusNum += bfs(virus[v]);
				}
				//cout << virusNum << endl;
				if (minVirus > virusNum)
				{
					minVirus = virusNum;
					x.first = blank[i].first;
					x.second = blank[i].second;
					y.first = blank[j].first;
					y.second = blank[j].second;
					z.first = blank[k].first;
					z.second = blank[k].second;
				}
				graph[blank[k].first][blank[k].second] = 0;
			}
			graph[blank[j].first][blank[j].second] = 0;
		}
		graph[blank[i].first][blank[i].second] = 0;
	}
	wallCnt += 3;
	cout << N * M << " " << wallCnt << " " << minVirus << " " << x.first << " " << x.second << " " << y.first << " " << y.second << " " << z.first << " " << z.second << endl;
	cout << N * M - wallCnt - minVirus;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	solve();
}