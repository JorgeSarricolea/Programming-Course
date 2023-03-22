import java.util.Scanner;

public class CrossProduct {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the length of the vectors: ");
        int length = input.nextInt();

        int[] vector1 = new int[length];
        int[] vector2 = new int[length];

        System.out.println("Enter the first vector: ");
        for (int i = 0; i < length; i++) {
            vector1[i] = input.nextInt();
        }

        System.out.println("Enter the second vector: ");
        for (int i = 0; i < length; i++) {
            vector2[i] = input.nextInt();
        }

        int[] crossProduct = new int[3];

        crossProduct[0] = (vector1[1] * vector2[2]) - (vector1[2] * vector2[1]);
        crossProduct[1] = (vector1[2] * vector2[0]) - (vector1[0] * vector2[2]);
        crossProduct[2] = (vector1[0] * vector2[1]) - (vector1[1] * vector2[0]);

        System.out.println("The cross product of the two vectors is: ");
        System.out.print("<" + crossProduct[0] + ", " + crossProduct[1] + ", " + crossProduct[2] + ">");
        input.close();
    }
}
