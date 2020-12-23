package leetcode;

public class FirstUniqChar {

    public int firstUniqChar(String s) {
        int[] cnt = new int[26];

        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (cnt[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] argv) {
        FirstUniqChar s = new FirstUniqChar();

        System.out.println(s.firstUniqChar(""));
        System.out.println(s.firstUniqChar("leetcode"));
        System.out.println(s.firstUniqChar("loveleetcode"));
    }
}
