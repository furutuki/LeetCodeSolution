
public class DecodeMethodCount {
    public int numDecodings(String s) {
        if (s.length() == 0) {
            return 0;
        }
        // dp[i]表示前i个字符一共多少种解码方式
        int[] dp = new int[s.length() + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;
        for (int i = 2; i <= s.length(); i++) {
            if (s.charAt(i - 2) == '1' || s.charAt(i - 2) == '2' && s.charAt(i - 1) < '7') { // [10, 26]
                if (s.charAt(i - 1) == '0') { // 10 or 20
                    dp[i] = dp[i - 2];
                } else {
                    dp[i] = dp[i - 2] + dp[i - 1];
                }
            } else {
                if (s.charAt(i - 1) == '0') {
                    return 0;
                } else {
                    dp[i] = dp[i - 1];
                }
            }
        }
        return dp[s.length()];
    }

    public static void main(String[] argv) {
        DecodeMethodCount s = new DecodeMethodCount();
        System.out.println(s.numDecodings("12"));
    }
}
