/* Create a program that takes in a matrix of integers and computes the transpose of the matrix. The transpose of a matrix is obtained by interchanging its rows and columns.
The program should then print out the resulting transposed matrix. */

import java.util.Scanner;

public class MatrixTranspose {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input the matrix size
        System.out.print("Enter the number of rows: ");
        int rows = scanner.nextInt();
        System.out.print("Enter the number of columns: ");
        int cols = scanner.nextInt();

        // Input the matrix elements
        int[][] matrix = new int[rows][cols];
        System.out.println("Enter the matrix elements:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }

        // Compute the transpose of the matrix
        int[][] transpose = new int[cols][rows];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transpose[j][i] = matrix[i][j];
            }
        }

        // Print out the transposed matrix
        System.out.println("The transposed matrix is:");
        for (int i = 0; i < cols; i++) {
            for (int j = 0; j < rows; j++) {
                System.out.print(transpose[i][j] + " ");
            }
            System.out.println();
        }

        scanner.close();
    }

}

