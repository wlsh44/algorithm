package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _14440 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int a0 = Integer.parseInt(st.nextToken());
        int a1 = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int T = 0;

        int[] dp = new int[n + 1];
        dp[0] = a0;
        dp[1] = a1;
        for (int i = 2; i <= n; i++) {
            dp[i] = (x * dp[i - 1] + y * dp[i - 2]) % 100;
            System.out.println(dp[i]);
            if (dp[i] == a1 && dp[i - 1] == a0) {
                T = i - 1;
                System.out.println("T: " + T);
                break;
            }
        }
        if (T != 0) {
            System.out.println(dp[n - (n / T) * T]);
        } else {
            System.out.println(dp[n]);
        }
    }
}
