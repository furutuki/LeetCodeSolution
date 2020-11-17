import java.util.ArrayList;

public class AllCellsDistOrder {

    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int maxDist = Math.max(r0, R - 1 - r0) + Math.max(c0, C - 1 - c0);

        ArrayList<ArrayList<int[]>> bucket = new ArrayList<>(maxDist + 1);
        for (int i = 0; i <= maxDist; i++) {
            bucket.add(new ArrayList<>());
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int dist = dist(i, j, r0, c0);
                ArrayList<int[]> list = bucket.get(dist);
                list.add(new int[]{i, j});
            }
        }

        int cnt = 0;
        int[][] ans = new int[R * C][2];
        for (int i = 0; i <= maxDist; i++) {
            ArrayList<int[]> list = bucket.get(i);
            if (!list.isEmpty()) {
                for (int[] pair : list) {
                    ans[cnt][0] = pair[0];
                    ans[cnt][1] = pair[1];
                    cnt++;
                }
            }
        }
        return ans;
    }

    private int dist(int sr, int sc, int dr, int dc) {
        return Math.abs(sr - dr) + Math.abs(sc - dc);
    }

    public static void main(String[] argv) {
        int[][] ans = new AllCellsDistOrder().allCellsDistOrder(1, 2, 0, 0);
        System.out.println(ans.length);
    }
}
