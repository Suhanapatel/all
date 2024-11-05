public class NQueens {
    private int[][] board;
    private int n;

    public NQueensfinal(int n, int firstRow, int firstCol) {
        this.n = n;
        board = new int[n][n];
        board[firstRow][firstCol] = 1; // Place the first queen

        // Start from the row after the first queen placement
        if (!placeQueens(firstRow + 1)) {
            System.out.println("No solution exists.");
        } else {
            printBoard();
        }
    }

    private boolean placeQueens(int row) {
        if (row == n) return true; // All queens placed successfully

        // Try to place a queen in each column of the current row
        for (int col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                board[row][col] = 1; // Place queen
                if (placeQueens(row + 1)) return true; // Recurse to place next queen
                board[row][col] = 0; // Backtrack if placement doesn't lead to a solution
            }
        }
        return false; // No valid placement found for this row
    }

    private boolean isSafe(int row, int col) {
        // Check this column for other queens
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1) return false;
        }

        // Check upper-left diagonal
        for (int i = 0; i < row; i++) {
            if (col - (row - i) >= 0 && board[i][col - (row - i)] == 1) return false;
        }

        // Check upper-right diagonal
        for (int i = 0; i < row; i++) {
            if (col + (row - i) < n && board[i][col + (row - i)] == 1) return false;
        }

        return true; // Safe to place queen at (row, col)
    }

    private void printBoard() {
        // Print the board with 1's representing queens and 0's representing empty spaces
        for (int[] row : board) {
            for (int cell : row) System.out.print(cell + " ");
            System.out.println();
        }
    }

    public static void main(String[] args) {
        new NQueens(4, 0, 1); // Correct placement of the first queen at (0, 1)
    }
}
