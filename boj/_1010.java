package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1010 {
    public static int N;
    public static int M;
    public static int[][] dp;

    public static int rec(int n, int m) {
        if (n == 1) {
            return m;
        }
        if (dp[n][m] != 0) {
            return dp[n][m];
        }
        for (int i = n - 1; i < m; i++) {
            dp[n][m] += rec(n - 1, i);
        }
        return dp[n][m];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());


        for (int t = 0; t < T; t++) {
            dp = new int[30][30];
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());


            System.out.println(rec(N, M));
        }
    }
}
