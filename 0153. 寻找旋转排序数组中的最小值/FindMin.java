package leetcode;

public class FindMin {

    public int findMin(int[] nums) {
        return solve(nums, 0, nums.length - 1);
    }

    private int solve(int[] nums, int low, int high) {
        if (low > high) {
            return Integer.MAX_VALUE;
        } else if (nums[low] <= nums[high]) {
            return nums[low];
        } else {
            int mid = low + (high - low) / 2;
            return Math.min(solve(nums, low, mid), solve(nums, mid + 1, high));
        }
    }
}
