/* Multiplication of two matrices. */

import java.util.Scanner;

public class MatrixMultiplication {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input dimensions of matrices
        System.out.print("Enter number of rows for matrix A: ");
        int rowsA = sc.nextInt();
        System.out.print("Enter number of columns for matrix A: ");
        int colsA = sc.nextInt();
        System.out.print("Enter number of rows for matrix B: ");
        int rowsB = sc.nextInt();
        System.out.print("Enter number of columns for matrix B: ");
        int colsB = sc.nextInt();

        // Check if matrices can be multiplied
        if (colsA != rowsB) {
            System.out.println("Error: The number of columns in matrix A must equal the number of rows in matrix B.");
        }

        // Input elements of matrix A
        System.out.println("Enter the elements of matrix A:");
        int[][] matrixA = new int[rowsA][colsA];
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsA; j++) {
                System.out.print("A[" + i + "][" + j + "]: ");
                matrixA[i][j] = sc.nextInt();
            }
        }

        // Input elements of matrix B
        System.out.println("Enter the elements of matrix B:");
        int[][] matrixB = new int[rowsB][colsB];
        for (int i = 0; i < rowsB; i++) {
            for (int j = 0; j < colsB; j++) {
                System.out.print("B[" + i + "][" + j + "]: ");
                matrixB[i][j] = sc.nextInt();
            }
        }

        // Multiply matrices
        int[][] result = new int[rowsA][colsB];
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        // Print result
        System.out.println("Result:");
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }

        sc.close();
    }
}
