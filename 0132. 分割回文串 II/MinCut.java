package leetcode;

public class MinCut {

    public int minCut(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        boolean[][] isPalindrome = new boolean[s.length()][s.length()];
        for (int j = 0; j < s.length(); j++) {
            for (int i = j; i >= 0; i--) {
                if (i == j) {
                    isPalindrome[i][j] = true;
                } else if (j - i == 1) {
                    isPalindrome[i][j] = (s.charAt(i) == s.charAt(j));
                } else {
                    isPalindrome[i][j] = (s.charAt(i) == s.charAt(j) && isPalindrome[i + 1][j - 1]);
                }
            }
        }

        // dp[i] 表示【0，i】区间的字符串分隔的最小次数
        int[] dp = new int[s.length()];
        for (int i = 1; i < s.length(); i++) {
            if (isPalindrome[0][i]) {
                dp[i] = 0;
                continue;
            }
            dp[i] = dp[i - 1] + 1;
            int min = dp[i];
            for (int j = 0; j < i; j++) {
                if (isPalindrome[j + 1][i]) {
                    min = Math.min(min, dp[j] + 1);
                }
            }
            dp[i] = min;
        }

        return dp[s.length() - 1];
    }

}
