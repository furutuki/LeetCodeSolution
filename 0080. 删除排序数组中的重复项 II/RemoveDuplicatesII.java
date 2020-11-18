public class RemoveDuplicatesII {

    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int left = 0;
        int right = left;
        int prevVal = nums[left];
        while (right < nums.length) {
            int cnt = 0;
            while (right < nums.length && nums[right] == prevVal) {
                right++;
                cnt++;
            }
            if (cnt >= 2) {
                nums[left++] = prevVal;
                nums[left++] = prevVal;
            } else {
                nums[left++] = prevVal;
            }
            if (right < nums.length) {
                prevVal = nums[right];
            }
        }
        return left;
    }

}
