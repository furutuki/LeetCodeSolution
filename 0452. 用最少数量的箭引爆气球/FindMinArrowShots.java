import java.util.Arrays;
import java.util.Comparator;

public class FindMinArrowShots {

    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }

        Arrays.sort(points, new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });

        int[] tmp = points[0];
        int ans = 1;
        int k = 1;
        while (k < points.length) {
            while (k < points.length && points[k][0] <= tmp[1]) {
                tmp[0] = Math.max(tmp[0], points[k][0]);
                tmp[1] = Math.min(tmp[1], points[k][1]);
                k++;
            }

            if (k < points.length) {
                tmp = points[k];
                ans++;
                k++;
            }
        }

        return ans;
    }
}
