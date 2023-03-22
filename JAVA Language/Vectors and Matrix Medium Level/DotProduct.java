import java.util.Scanner;

public class DotProduct {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the length of the vectors: ");
        int n = sc.nextInt();

        int[] v1 = new int[n];
        int[] v2 = new int[n];

        System.out.println("Enter the elements of the first vector:");
        for (int i = 0; i < n; i++) {
            v1[i] = sc.nextInt();
        }

        System.out.println("Enter the elements of the second vector:");
        for (int i = 0; i < n; i++) {
            v2[i] = sc.nextInt();
        }

        int dotProduct = 0;
        for (int i = 0; i < n; i++) {
            dotProduct += v1[i] * v2[i];
        }

        System.out.println("The dot product of the two vectors is: " + dotProduct);

        sc.close();
    }
}
