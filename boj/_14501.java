package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _14501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] T = new int[16];
        int[] P = new int[16];
        int[] dp = new int[16];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
//            if (T[i] + i > N + 1) {
//                P[i] = 0;
//            }
        }

//        for (int i = 1; i <= N; i++) {
//            for (int j = 1; j <= i; j++) {
//                if (T[j] + j <= i) {
//                    dp[i] = Math.max(P[i] + dp[j], dp[i]);
//                } else {
//                    dp[i] = Math.max(P[i], dp[i]);
//                }
//            }
//        }
        int max = 0;
        for (int i = 1; i <= N + 1; i++) {
            dp[i] = Math.max(dp[i], max);
            if (T[i] + i <= N + 1) {
                dp[T[i] + i] = Math.max(dp[i] + P[i], dp[T[i] + i]);
            }
            max = Math.max(dp[i], max);
        }
        System.out.println(max);
    }
}
