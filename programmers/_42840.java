package programmers;

import java.util.ArrayList;
import java.util.Arrays;

public class _42840 {
            public static int[] solution(int[] answers) {
                int[] answer = {};
                int[] supo1 = {1, 2, 3, 4, 5};
                int[] supo2 = {2, 1, 2, 3, 2, 4, 2, 5};
                int[] supo3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
                int[] num = {0, 0, 0};
                int max = 0;

                for (int i = 0; i < answers.length; i++) {
                    if (supo1[i % 5] == answers[i]) num[0]++;
                    if (supo2[i % 8] == answers[i]) num[1]++;
                    if (supo3[i % 10] == answers[i]) num[2]++;
                }
                max = Arrays.stream(num).max().getAsInt();
                ArrayList<Integer> temp = new ArrayList<>();
                for (int i = 0; i < 3; i++) {
                    if (num[i] == max) temp.add(i + 1);
                }
                answer = new int[temp.size()];
                for (int i = 0; i < temp.size(); i++) {
                    answer[i] = temp.get(i);
                }
                return answer;

    }
    public static void run() {
        int[] answers = {1, 2, 3, 4, 5};
        int[] answers2 = {1, 3, 2, 4, 2};
        int[] answers3 = {1, 1, 1, 2, 1};
        int ans[] = _42840.solution(answers3);
        for (int i = 0; i < ans.length; i++)
            System.out.println(ans[i] + " ");
    }
}
