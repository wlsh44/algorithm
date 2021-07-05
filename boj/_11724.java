package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class _11724 {
    public static int[][] graph = new int[1001][1001];
    public static boolean[] visit = new boolean[1001];
    public static int N;
    public static int M;

    public static void dfs(int node) {
        Queue<Integer> q = new LinkedList<>();
        q.add(node);
        visit[node] = true;

        while (!q.isEmpty()) {
            int n = q.peek(); q.remove();

            for (int i = 1; i <= N; i++) {
                if (graph[n][i] == 1 && !visit[i]) {
                    visit[i] = true;
                    q.add(i);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int count = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            graph[n1][n2] = 1;
            graph[n2][n1] = 1;
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                if (!visit[i]) {
                    dfs(i);
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
