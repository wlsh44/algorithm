package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _10844 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] dp = new int[100][10];
        long sum = 0;

        for (int i = 1; i < 10; i++) {
            dp[0][i] = 1;
        }
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][j + 1] % 1000000000;
                } else if (j == 9) {
                    dp[i][j] = dp[i - 1][j - 1] % 1000000000;
                } else {
                    dp[i][j] = (dp[i - 1][j + 1] + dp[i - 1][j - 1]) % 1000000000;
                }
            }
        }
        for (int num : dp[N - 1]) {
            sum += num;
        }
        System.out.println(sum % 1000000000);
    }
}
