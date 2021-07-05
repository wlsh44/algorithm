package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class _10989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        int[] arr = new int[10001];

        for (int i = 0; i < N; i++) {
            arr[Integer.parseInt(br.readLine())]++;
        }

        for (int i = 1; i <= 10000; i++) {
            while (arr[i] != 0) {
                sb.append(i + "\n");
                arr[i]--;
            }
        }
        System.out.println(sb);
    }
}
