package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class _1149 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] cost = new int[1001][3];
        final int RED = 0;
        final int GREEN = 1;
        final int BLUE = 2;

        StringTokenizer st = new StringTokenizer(br.readLine());
        cost[0][RED] = Integer.parseInt(st.nextToken());
        cost[0][GREEN] = Integer.parseInt(st.nextToken());
        cost[0][BLUE] = Integer.parseInt(st.nextToken());

        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            cost[i][RED] = Integer.parseInt(st.nextToken()) + Math.min(cost[i - 1][GREEN], cost[i - 1][BLUE]);
            cost[i][GREEN] = Integer.parseInt(st.nextToken()) + Math.min(cost[i - 1][RED], cost[i - 1][BLUE]);
            cost[i][BLUE] = Integer.parseInt(st.nextToken()) + Math.min(cost[i - 1][GREEN], cost[i - 1][RED]);
        }
        System.out.println(Math.min(Math.min(cost[N - 1][RED], cost[N - 1][GREEN]), cost[N - 1][BLUE]));
    }
}
