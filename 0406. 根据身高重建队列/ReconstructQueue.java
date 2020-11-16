import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;

public class ReconstructQueue {
    public int[][] reconstructQueue(int[][] people) {
        if (people.length == 0) {
            return new int[0][0];
        }
        Arrays.sort(people, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                } else {
                    return o2[0] - o1[0];
                }
            }
        });

        LinkedList<int[]> tmp = new LinkedList<>();
        for (int[] person : people) {
            tmp.add(person[1], person);
        }
        return tmp.toArray(new int[people.length][people[0].length]);
    }
}
