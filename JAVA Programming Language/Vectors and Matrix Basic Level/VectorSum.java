/* Program Sum of two vectors. */

import java.util.Scanner;

public class VectorSum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the size of the vectors: ");
        int n = input.nextInt();

        int[] vector1 = new int[n];
        int[] vector2 = new int[n];
        int[] sum = new int[n];

        System.out.println("Enter the elements of the first vector: ");
        for (int i = 0; i < n; i++) {
            vector1[i] = input.nextInt();
        }

        System.out.println("Enter the elements of the second vector: ");
        for (int i = 0; i < n; i++) {
            vector2[i] = input.nextInt();
        }

        for (int i = 0; i < n; i++) {
            sum[i] = vector1[i] + vector2[i];
        }

        System.out.print("The sum of the two vectors is: ");
        for (int i = 0; i < n; i++) {
            System.out.print(sum[i] + " ");
        }

        input.close();
    }
}
