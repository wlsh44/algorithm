package leetcode.maxStack;

public class Test {

    public static void main(String[] args) {
        MaxStack stack = new MaxStack();

        stack.push(5);
        stack.push(1);
        stack.push(5);
        System.out.println(stack.top()); // return 5
        System.out.println(stack.popMax()); // return 5
        System.out.println(stack.top()); // return 1
        System.out.println(stack.peekMax()); // return 5
        System.out.println(stack.pop()); // return 1
        System.out.println(stack.top()); // return 5
    }
}
