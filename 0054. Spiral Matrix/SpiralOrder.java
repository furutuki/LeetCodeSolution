package leetcode;

import java.util.ArrayList;
import java.util.List;

public class SpiralOrder {

    private void search(int[][] matrix, List<Integer> res, int top, int bottom, int left, int right, int direction) {
        if (top > bottom || left > right) {
            return;
        }

        if (top == bottom && left == right) {
            res.add(matrix[top][left]);
            return;
        }

        if (direction == 0) { // towards right
            for (int col = left; col <= right; col++) {
                res.add(matrix[top][col]);
            }
            search(matrix, res, top + 1, bottom, left, right, 1);
        } else if (direction == 1) { // towards bottom
            for (int row = top; row <= bottom; row++) {
                res.add(matrix[row][right]);
            }
            search(matrix, res, top, bottom, left, right - 1, 2);
        } else if (direction == 2) { // towards left
            for (int col = right; col >= left; col--) {
                res.add(matrix[bottom][col]);
            }
            search(matrix, res, top, bottom - 1, left, right, 3);
        } else if (direction == 3) { // towards up
            for (int row = bottom; row >= top; row--) {
                res.add(matrix[row][left]);
            }
            search(matrix, res, top, bottom, left + 1, right, 0);
        }
    }
    public List<Integer> spiralOrder(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        ArrayList<Integer> res = new ArrayList<>();
        search(matrix, res, 0, row - 1, 0, col - 1, 0);
        return res;
    }


    public static void main(String[] args) {
        SpiralOrder solution = new SpiralOrder();
        int[][] param = {{1,2,3},{4,5,6},{7,8,9}};
        List<Integer> res = solution.spiralOrder(param);
        for (int n : res) {
            System.out.println(n + " ");
        }
    }

}
