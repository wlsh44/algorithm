package leetcode;

import java.util.*;

class HitCounter {

    private final Stack<Integer> stack = new Stack<>();

    public void hit(int timestamp) {
        stack.push(timestamp);
    }

    public int getHits(int timestamp) {
        int sum = 0;
        Stack<Integer> s = (Stack<Integer>) stack.clone();

        while (!s.isEmpty() && s.pop() > timestamp - 300) {
            sum++;
        }
        return sum;
    }

//    private final Map<Integer, Integer> map = new HashMap<>();
//
//    public void hit(int timestamp) {
//        map.put(timestamp, map.getOrDefault(timestamp, 0) + 1);
//    }
//
//    public int getHits(int timestamp) {
//        return map.entrySet().stream()
//                .filter(x -> x.getKey() > timestamp - 300 && x.getKey() <= timestamp)
//                .map(Map.Entry::getValue)
//                .mapToInt(Integer::intValue)
//                .sum();
//    }
}

public class _362 {
    public static void main(String[] args) {
        HitCounter counter = new HitCounter();
        System.out.println(counter.getHits(1));
        counter.hit(1); // timestamp 1에 hit 기록
        counter.hit(2); // timestamp 2에 hit 기록
        counter.hit(3); // timestamp 3에 hit 기록
        System.out.println(counter.getHits(3)); // timestamp 4로부터 최근 5분간의 hit수인 3을 return
        System.out.println(counter.getHits(4)); // timestamp 4로부터 최근 5분간의 hit수인 3을 return
        counter.hit(300); // timestamp 300에 hit 기록
        System.out.println(counter.getHits(300)); // timestamp 300으로부터 최근 5분간의 hit수인 4를 리턴
        System.out.println(counter.getHits(301)); // timestamp 301로부터 최근 5분간의 hit 수인 3을 리턴
//
//        for (int i = 0; i < 5000; i++) {
//            counter.hit(i);
//        }
//        System.out.println(counter.getHits(4500));
    }
}
