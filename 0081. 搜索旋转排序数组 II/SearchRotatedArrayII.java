package leetcode;

public class SearchRotatedArrayII {

    public boolean search(int[] nums, int target) {
        return solve(nums, 0, nums.length - 1, target);
    }

    private boolean solve(int[] nums, int low, int high, int target) {
        if (nums.length == 0 || low > high) {
            return false;
        }

        if (nums[low] < nums[high]) {
            return searchDivideAndConquer(nums, low, high, target);
        } else {
            int mid = (low + high) / 2;
            return nums[mid] == target || solve(nums, low, mid - 1, target) || solve(nums, mid + 1, high, target);
        }
    }

    private boolean searchDivideAndConquer(int[] nums, int low, int high, int target) {
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }

}
