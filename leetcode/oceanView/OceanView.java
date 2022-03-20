package leetcode.oceanView;

import java.util.*;

public class OceanView {

    public static int[] findOceanViewBuildings(int[] heights) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < heights.length; i++) {
            while (!stack.isEmpty() && heights[stack.peek()] <= heights[i]) {
                stack.pop();
            }
            stack.push(i);
        }
        return stack.stream().mapToInt(x -> x).toArray();
    }

    public static void print(int[] output) {
        for (int i = 0; i < output.length; i++) {
            System.out.println(output[i]);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        print(findOceanViewBuildings(new int[]{4, 2, 3, 1}));
        print(findOceanViewBuildings(new int[]{4, 3, 2, 1}));
        print(findOceanViewBuildings(new int[]{1, 3, 2, 4}));
        print(findOceanViewBuildings(new int[]{2, 2, 2, 2}));
        print(findOceanViewBuildings(new int[]{2}));
    }
}
