package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2156 {
    public static int[] arr = new int[10001];
    public static int[] dp = new int[10001];
    public static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        dp[0] = 0;
        dp[1] = arr[1];
        dp[2] = arr[1] + arr[2];
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(Math.max(dp[i - 1], dp[i - 2] + arr[i]), dp[i - 3] + arr[i - 1] + arr[i]);
        }
        System.out.println(dp[n]);
    }
}
