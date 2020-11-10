import java.util.HashMap;

public class LongestConsecutiveSequence3 {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int ans = 0;

        UnionFind unionFind = new UnionFind(nums);
        for (int item : nums) {
            unionFind.union(item, item + 1);
        }

        for (int item : nums) {
            ans = Math.max(ans, unionFind.find(item) - item + 1);
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

class UnionFind {

    private HashMap<Integer, Integer> parent;
    private int count;

    public UnionFind(int[] nums) {
        count = nums.length;
        parent = new HashMap<>();
        for (int item : nums) {
            parent.put(item, item);
        }
    }

    public Integer find(int item) {
        if (!parent.containsKey(item)) {
            return null;
        }

        int node = item;
        while (node != parent.get(node)) {
            node = parent.get(node);
        }
        return node;
    }

    public void union(int p, int q) {
        Integer rootP = find(p);
        Integer rootQ = find(q);

        if (rootP != null && rootP.equals(rootQ)) {
            return;
        }

        if (rootP == null || rootQ == null) {
            return;
        }

        parent.put(rootP, rootQ);
        count--;
    }
}
