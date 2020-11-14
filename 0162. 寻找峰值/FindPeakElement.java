class FindPeakElement {
    // 小trick，直接找最大值即可
    public int findPeakElement(int[] nums) {
        int index = 0;
        int item = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > item) {
                item = nums[i];
                index = i;
            }
        }
        return index;
    }
}