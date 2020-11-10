class SetZeroForMatrix {
    public void setZeroes(int[][] matrix) {
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();
        int row = matrix.length;
        int col = matrix[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }

        for (Integer r : rows) {
            for (int c = 0; c < col; c++) {
                matrix[r][c] = 0;
            }
        }

        for (Integer c : cols) {
            for (int r = 0; r < row; r++) {
                matrix[r][c] = 0;
            }
        }
    }
}