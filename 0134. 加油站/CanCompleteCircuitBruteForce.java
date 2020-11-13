public class CanCompleteCircuitBruteForce {

    public int canCompleteCircuit(int[] gas, int[] cost) {
        for (int i = 0; i < gas.length; i++) {
            int g = gas[i];
            int j;
            for (j = 1; j <= gas.length; j++) {
                int curPos = (i + j - 1 + gas.length) % gas.length;
                int nextPos = (i + j + gas.length) % gas.length;
                if (g < cost[curPos]) {
                    break;
                }
                g += gas[nextPos] - cost[curPos];
            }
            if (j > gas.length) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] argv) {
        System.out.println(new CanCompleteCircuit().canCompleteCircuit(
                new int[] {3,3,4}, new int[] {3,4,4}
        ));
    }
}
