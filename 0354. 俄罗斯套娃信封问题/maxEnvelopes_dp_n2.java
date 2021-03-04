package leetcode;

import java.util.Arrays;
import java.util.Comparator;

public class MaxEnvelopes {

    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        int[] dp = new int[envelopes.length];
        Arrays.fill(dp, 1);
        int ret = 1;
        for (int i = 0; i < envelopes.length; i++) {
            for (int j = 0; j < i; j++) {
                if (envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            ret = Math.max(ret, dp[i]);
        }

        return ret;
    }

    public static void main(String[] argv) {
        MaxEnvelopes solution = new MaxEnvelopes();
        int[][] param = {{10,8}, {1,12}, {6,15}, {2,18}};
        System.out.println(solution.maxEnvelopes(param));
    }

}
