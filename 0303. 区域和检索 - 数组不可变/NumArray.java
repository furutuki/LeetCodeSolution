class NumArray {

    int preSum[];

    public NumArray(int[] nums) {
        int length = (nums != null? nums.length : 0);
        preSum = new int[length];
        for (int i = 0; i < length; i++) {
            preSum[i] = nums[i] + (i > 0 ? preSum[i - 1] : 0);
        }
    }

    public int sumRange(int i, int j) {
        return i > 0 ? preSum[j] - preSum[i - 1] : preSum[j];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */