import java.util.HashSet;

// 利用set特性，在O（1）时间内查询是否有下一个连续的数字
public class LongestConsecutiveSequece2 {

    public int longestConsecutive(int[] nums) {
        int ans = 0;
        HashSet<Integer> s = new HashSet<>();
        for (int item : nums) {
            s.add(item);
        }

        for (int item : nums) {
            if (s.contains(item - 1)) {
                continue;
            }

            int start = item;
            while (s.contains(item + 1)) {
                item += 1;
            }
            ans = Math.max(ans, item - start + 1);
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
