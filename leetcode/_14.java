package leetcode;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class _14 {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            int j = 0;
            while (j < prefix.length() && j < strs[i].length() && prefix.charAt(j) == strs[i].charAt(j)) {
                j++;
            }
            prefix = j == 0 ? "" : prefix.substring(0, j);
        }
        return prefix;
    }

    public static void main(String[] args) {
        _14 solution = new _14();
        System.out.println(solution.longestCommonPrefix(new String[] {"flower", "flow", "flight"}));
        System.out.println(solution.longestCommonPrefix(new String[] {"dog", "racecar", "car"}));
        System.out.println(solution.longestCommonPrefix(new String[] {"technically", "technic", "technology", "technical"}));
    }
}
