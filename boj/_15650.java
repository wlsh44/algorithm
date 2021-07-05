package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _15650 {
    public static boolean[] visit;
    public static int[] arr;
    public static StringBuilder sb = new StringBuilder();

    public static void dfs(int N, int M, int depth, int idx) {
        if (depth == M) {
            for (int num : arr) {
                sb.append(num).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = idx; i < N; i++) {
            if (!visit[i]) {
                visit[i] = true;
                arr[depth] = i + 1;
                dfs(N, M, depth + 1, i);
                visit[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        visit = new boolean[N];
        arr = new int[M];

        dfs(N, M, 0, 0);
        System.out.println(sb);
    }
}
