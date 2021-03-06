class Solution {
    public int numDistinct(String s, String t) {
        // dp[i][j]： T的前i个字符可以由S的前j个字符组成的最多方案数
        // T[i] == S[j]: dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        // T[i] != S[j]: dp[i][j] = dp[i][j - 1]

        int m = s.length();
        int n = t.length();
        int[][] dp = new int[n + 1][m + 1];
        for (int j = 0; j <= m; j++) {
            dp[0][j] = 1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s.charAt(j - 1) == t.charAt(i - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }
        return dp[n][m];
    }
}