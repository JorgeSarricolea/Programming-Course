import java.util.*;

public class MatrixSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int m = sc.nextInt();
        System.out.println("Enter the number of columns: ");
        int n = sc.nextInt();
        int[][] a = new int[m][n];
        int[][] b = new int[m][n];
        int[][] sum = new int[m][n];
        System.out.println("Enter the elements of the first matrix: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter the elements of the second matrix: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                b[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sum[i][j] = a[i][j] + b[i][j];
            }
        }
        System.out.println("The sum of the two matrices is: ");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(sum[i][j] + " ");
            }
            System.out.println();
        }
        sc.close();
    }
}
