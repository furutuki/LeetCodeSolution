package leetcode;

public class GenerateMatrix {

    private void search(int[][] matrix, int curNum, int top, int bottom, int left, int right, int direction) {
        if (top > bottom || left > right) {
            return;
        }

        if (top == bottom && left == right) {
            matrix[top][left] = curNum;
            return;
        }

        if (direction == 0) { // towards right
            for (int col = left; col <= right; col++) {
                matrix[top][col] = curNum++;
            }
            search(matrix, curNum, top + 1, bottom, left, right, 1);
        } else if (direction == 1) { // towards bottom
            for (int row = top; row <= bottom; row++) {
                matrix[row][right] = curNum++;
            }
            search(matrix, curNum, top, bottom, left, right - 1, 2);
        } else if (direction == 2) { // towards left
            for (int col = right; col >= left; col--) {
                matrix[bottom][col] = curNum++;
            }
            search(matrix, curNum, top, bottom - 1, left, right, 3);
        } else if (direction == 3) { // towards up
            for (int row = bottom; row >= top; row--) {
                matrix[row][left] = curNum++;
            }
            search(matrix, curNum, top, bottom, left + 1, right, 0);
        }
    }

    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        search(matrix, 1, 0, n - 1, 0, n - 1, 0);
        return matrix;
    }

}
