import java.util.Arrays;

// 排序数组再遍历一次
public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        int ans = 0;
        Arrays.sort(nums);
        int cur = 0;
        while (cur < nums.length) {
            int cnt = 1;
            while (cur + 1 < nums.length) {
                // 注意【1,2,0,1]应该返回3
                if (nums[cur] == nums[cur + 1]) {
                    cur += 1;
                    continue;
                }
                if (nums[cur] + 1!= nums[cur + 1]) {
                    break;
                }
                cur += 1;
                cnt += 1;
            }
            ans = Math.max(ans, cnt);
            cur += 1;
        }
        return ans;
    }

    public static void main(String[] argv) {
        LongestConsecutiveSequence solution = new LongestConsecutiveSequence();
        int ans = solution.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2});
        System.out.println(ans);
        System.out.println(solution.longestConsecutive(new int[]{0,3,7,2,5,8,4,6,0,1}));
        System.out.println(solution.longestConsecutive(new int[]{1, 2, 0, 1}));
    }
}
