public class MaxProduct {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) {
            return nums[0];
        }
        // dp[i][0]:以i结尾的子串乘积最小值
        // dp[i][1]:以i结尾的子串乘积最大值
        int[][] dp = new int[nums.length][2];

        dp[0][0] = nums[0];
        dp[0][1] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] >= 0) {
                dp[i][0] = Math.min(nums[i], dp[i - 1][0] * nums[i]);
                dp[i][1] = Math.max(nums[i], dp[i - 1][1] * nums[i]);
            } else {
                dp[i][0] = Math.min(nums[i], dp[i - 1][1] * nums[i]);
                dp[i][1] = Math.max(nums[i], dp[i - 1][0] * nums[i]);
            }
        }
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < dp.length; i++) {
            ans = Math.max(ans, dp[i][1]);
        }
        return ans;
    }

    public static void main(String[] argv) {
        MaxProduct s = new MaxProduct();
        System.out.println(s.maxProduct(new int[]{-2,3,4}));
    }
}
