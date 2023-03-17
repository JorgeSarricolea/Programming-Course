/* Sum of two matrices */

import java.util.Scanner;

public class MatrixSum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int rows, columns;

        // Read the dimensions of the matrices from the user
        System.out.print("Enter the number of rows: ");
        rows = input.nextInt();
        System.out.print("Enter the number of columns: ");
        columns = input.nextInt();

        // Create the matrices
        int[][] matrix1 = new int[rows][columns];
        int[][] matrix2 = new int[rows][columns];
        int[][] sumMatrix = new int[rows][columns];

        // Read the values of the first matrix from the user
        System.out.println("Enter the values of the first matrix: ");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix1[i][j] = input.nextInt();
            }
        }

        // Read the values of the second matrix from the user
        System.out.println("Enter the values of the second matrix: ");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix2[i][j] = input.nextInt();
            }
        }

        // Calculate the sum of the two matrices
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                sumMatrix[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }

        // Print the sum of the two matrices
        System.out.println("The sum of the two matrices is:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(sumMatrix[i][j] + " ");
            }
            System.out.println();

            input.close();
        }
    }
}
