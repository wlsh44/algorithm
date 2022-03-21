package leetcode;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        List<Integer> list = Arrays.stream(tickets).boxed().collect(Collectors.toList());
        Deque<Integer> queue = new ArrayDeque<>(list);

        int num = queue.pollFirst() - 1;
        int time = 1;
        while (!(num == 0 && k == 0)) {
            if (num != 0) {
                queue.addLast(num);
            }
            if (k == 0) {
                k = queue.size() - 1;
            } else {
                k--;
            }
            num = queue.pollFirst() - 1;
            time++;
        }
        return time;
    }

    public int timeRequiredToBuy2(int[] tickets, int k) {
        int time = 0;

        for (int i = 0; i < tickets.length; i++) {
            if (i <= k) {
                time += Math.min(tickets[i], tickets[k]);
            } else {
                time += Math.min(tickets[i], tickets[k] - 1);
            }
        }
        return time;
    }
}

public class _2073 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.timeRequiredToBuy2(new int[] {2, 3, 2}, 2));
        System.out.println(solution.timeRequiredToBuy2(new int[] {5, 1, 1, 1}, 0));
    }
}
