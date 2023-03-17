/* Program to find the greatest common divisor (GCD) of two positive integer numbers. */

import java.util.Scanner;

public class GCD {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first positive integer: ");
        int num1 = input.nextInt();

        System.out.print("Enter the second positive integer: ");
        int num2 = input.nextInt();

        int gcd = findGCD(num1, num2);

        System.out.println("The greatest common divisor of " + num1 + " and " + num2 + " is " + gcd);
    }

    public static int findGCD(int num1, int num2) {
        while (num2 != 0) {
            int temp = num2;
            num2 = num1 % num2;
            num1 = temp;
        }
        return num1;
    }
}
