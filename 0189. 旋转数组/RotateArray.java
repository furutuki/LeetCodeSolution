public class RotateArray {

    private void reverse(int[] nums, int start, int end) {
        int m = start;
        int n = end;
        while (m < n) {
            int tmp = nums[m];
            nums[m] = nums[n];
            nums[n] = tmp;
            m++;
            n--;
        }
    }

    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }
}
