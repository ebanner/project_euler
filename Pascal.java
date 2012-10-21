import java.math.BigInteger;


public class Pascal {

    public static void main(String[] args) {
        BigInteger[][] grid = new BigInteger[20][20];

        for (int i = 0; i < 20; i++) {
            grid[0][i] = 1;
            grid[i][0] = 1;
        }

        for (int i = 1; i < 20; i++) {
            for (int j = 1; j < 20; j++) {
                grid[i][j] = grid[i][j-1] + grid[i-1][j];
            }
        }

        System.out.println(grid[3][3]);
    }
}
