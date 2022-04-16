package leetcode;

import java.util.Arrays;

public class _88 {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tmp = Arrays.copyOf(nums1, nums1.length);
        int i = 0;
        int j = 0;
        int k = 0;

        while (i < m && j < n) {
            if (tmp[i] < nums2[j]) {
                nums1[k++] = tmp[i++];
            } else {
                nums1[k++] = nums2[j++];
            }
        }

        if (i == m) {
            while (j < n) {
                nums1[k++] = nums2[j++];
            }
        } else {
            while (i < m) {
                nums1[k++] = tmp[i++];
            }
        }
    }

    public static void main(String[] args) {
        _88 solution = new _88();

        int[] list = new int[] {1, 2, 3, 0, 0, 0};
        solution.merge(list, 3, new int[] {2, 5, 6}, 3);
        for (int i = 0; i < 6; i++) {
            System.out.println("list[i] = " + list[i]);
        }

        list = new int[] {2,5,6,7,0,0};
        solution.merge(list, 4, new int[] {1, 8}, 2);
        for (int i = 0; i < 6; i++) {
            System.out.println("list[i] = " + list[i]);
        }
    }
}
