package programmers;

public class _72410 {
        public static String step1(String new_id) {
            return new_id.toLowerCase();
        }

        public static String step2(String new_id) {
//            StringBuffer buf = new StringBuffer();
//
//            for (int i = 0; i < new_id.length(); i++) {
//                if (((new_id.charAt(i) >= 'a' && new_id.charAt(i) <= 'z') ||
//                        (new_id.charAt(i) >= '0' && new_id.charAt(i) <= '9') ||
//                        new_id.charAt(i) == '-' || new_id.charAt(i) == '_' ||
//                        new_id.charAt(i) == '.'))
//                    buf.append(new_id.charAt(i));
//            }
//            return buf.toString();
            return new_id.replaceAll("[^-_.a-z0-9]", "");
        }

        public static String step3(String new_id) {
//            StringBuffer buf = new StringBuffer();
//            int i = 0;
//
//            while (i < new_id.length()) {
//                buf.append(new_id.charAt(i));
//                if (new_id.charAt(i) == '.') {
//                    while (i < new_id.length() && new_id.charAt(i) == '.')
//                        i++;
//                }
//                else
//                    i++;
//            }
//            return buf.toString();
            return new_id.replaceAll("[.]{2,}", ".");
        }

        public static String step4(String new_id) {
//            StringBuffer buf = new StringBuffer(new_id);
//
//            if (buf.charAt(0) == '.')
//                buf.deleteCharAt(0);
//            if (buf.length() != 0 && buf.charAt(buf.length() - 1) == '.')
//                buf.deleteCharAt(buf.length() - 1);
//            return buf.toString();

            return new_id.replaceAll("^[.][.]$", "");
        }

        public static String step5(String new_id) {
            if (new_id.isEmpty()) {
                return "a";
            }
            return new_id;
        }

        public static String step6(String new_id) {
            if (new_id.length() > 15) {
                String temp = new_id.substring(0, 15);
//                return step4(temp);
                return temp.replaceAll("[.]$", "");
            }
            return new_id;
        }

        public static String step7(String new_id) {
            if (new_id.length() <= 2) {
                String temp = new_id;

                char ch = new_id.charAt(new_id.length() - 1);
                while (temp.length() < 3)
                    //temp.append(ch);
                    temp += ch;
                return temp;
            }
            return new_id;
        }

        public static String solution(String new_id) {
            String answer = "";
            String temp = new_id;

            temp = step1(temp);
            temp = step2(temp);
            temp = step3(temp);
            temp = step4(temp);
            temp = step5(temp);
            temp = step6(temp);
            answer = step7(temp);

            return answer;
        }

    public static void run() {
        System.out.println(_72410.solution("...!@BaT#*..y.abcdefghijklm"));
        System.out.println(_72410.solution("z-+.^."));
        System.out.println(_72410.solution("=.="));
        System.out.println(_72410.solution("123_.def"));
        System.out.println(_72410.solution("abcdefghijklmn.p"));
    }
}
