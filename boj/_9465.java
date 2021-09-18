package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _9465 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[][] P = new int[N + 1][2];
            int[][] dp = new int[N + 1][2];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                P[i][0] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                P[i][1] = Integer.parseInt(st.nextToken());
            }
            dp[0][0] = P[0][0];
            dp[0][1] = P[0][1];
            dp[1][0] = P[0][1] + P[1][0];
            dp[1][1] = P[0][0] + P[1][1];
            for (int i = 2; i < N; i++) {
                dp[i][0] = Math.max(dp[i - 1][1], dp[i - 2][1]) + P[i][0];
                dp[i][1] = Math.max(dp[i - 1][0], dp[i - 2][0]) + P[i][1];
            }
            System.out.println(Math.max(dp[N - 1][0], dp[N - 1][1]));
        }
    }
}
