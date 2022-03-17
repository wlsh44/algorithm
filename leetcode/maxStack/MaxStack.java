package leetcode.maxStack;

import java.util.*;

public class MaxStack {

    private List<Integer> list = new ArrayList<>();

    public void push(int x) {
        list.add(x);
    }

    public int pop() {
        int x = list.get(0);
        list.remove(0);

        return x;
    }

    public int top() {
        return list.get(0);
    }

    public int peekMax() {
        return Collections.max(list);
    }

    public int popMax() {
        Integer max = Collections.max(list);
        list.remove(max);

        return max;
    }
}
