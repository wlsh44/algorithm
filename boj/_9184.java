package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class _9184 {
    public static int[][][] dp = new int[21][21][21];

    public static int rec(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return 1;
        } else if (a > 20 || b > 20 || c > 20) {
            return dp[20][20][20] = rec(20, 20, 20);
        }
        if (dp[a][b][c] != 0) {
            return dp[a][b][c];
        } else if (a < b && b < c) {
            return dp[a][b][c] = rec(a, b, c - 1) + rec(a, b - 1, c - 1) - rec(a, b - 1, c);
        } else {
            return dp[a][b][c] = rec(a - 1, b, c) + rec(a - 1, b - 1, c) + rec(a - 1, b, c - 1) - rec(a - 1, b - 1, c - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == -1 && b == -1 && c == -1) {
                break;
            }
            sb.append("w(").append(a).append(", ")
                    .append(b).append(", ")
                    .append(c).append(") = ")
                    .append(rec(a, b, c)).append("\n");
        }
        System.out.println(sb);
    }
}
