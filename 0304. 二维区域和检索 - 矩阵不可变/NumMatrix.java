package leetcode;

public class NumMatrix {

    private int[][] preSum;

    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        preSum = new int[matrix.length][matrix[0].length];
        for (int j = 0; j < matrix[0].length; j++) {
            preSum[0][j] = (j > 0 ? preSum[0][j - 1] : 0) + matrix[0][j];
        }
        for (int i = 0; i < matrix.length; i++) {
            preSum[i][0] = (i > 0 ? preSum[i - 1][0] : 0) + matrix[i][0];
        }

        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] + matrix[i][j] - preSum[i - 1][j - 1];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int topPreSum = (row1 > 0 ? preSum[row1 - 1][col2] : 0);
        int leftPreSum = (col1 > 0 ? preSum[row2][col1 - 1] : 0);
        int leftTopPreSum = (row1 > 0 && col1 > 0 ? preSum[row1 - 1][col1 - 1] : 0);
        return preSum[row2][col2] - leftPreSum - topPreSum + leftTopPreSum;
    }

    public static void main(String[] argv) {
        int[][] matrix = {
                {3, 0, 1, 4, 2},
                {5, 6, 3, 2, 1},
                {1, 2, 0, 1, 5},
                {4, 1, 0, 1, 7},
                {1, 0, 3, 0, 5}
        };

        NumMatrix solution = new NumMatrix(matrix);

        System.out.println(solution.sumRegion(2, 1, 4, 3));

        System.out.println(solution.sumRegion(1,1,2,2));

        System.out.println(solution.sumRegion(1,2,2,4));
    }
}
