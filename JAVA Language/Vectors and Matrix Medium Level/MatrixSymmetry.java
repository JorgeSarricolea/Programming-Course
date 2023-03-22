/* Create a program that takes in a matrix of integers and checks whether or not it is symmetric. A matrix is symmetric if it is equal to its transpose.
The program should print out whether or not the matrix is symmetric. */

import java.util.Scanner;

public class MatrixSymmetry {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input the size of the matrix
        System.out.print("Enter the number of rows/columns for the matrix: ");
        int size = scanner.nextInt();

        // Input the elements of the matrix
        int[][] matrix = new int[size][size];
        System.out.println("Enter the elements of the matrix:");
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }

        // Check if the matrix is symmetric
        boolean isSymmetric = true;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (matrix[i][j] != matrix[j][i]) {
                    isSymmetric = false;
                    break;
                }
            }
            if (!isSymmetric) {
                break;
            }
        }

        // Print out whether or not the matrix is symmetric
        if (isSymmetric) {
            System.out.println("The matrix is symmetric.");
        } else {
            System.out.println("The matrix is not symmetric.");
        }

        scanner.close();
    }

}
